## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 The modelling cycle

Every problem in this topic has the same five-stage shape, and the marks are distributed across the stages rather than concentrated in the algebra.

The first stage selects the state variable: the single quantity whose value at time $t$ summarises the situation. For a cooling body it is the temperature, for a tank it is the mass of dissolved substance, for a circuit it is the charge or the current, and for two springs it is the pair of displacements.

The second stage invokes a physical law. The law is always a statement about a rate, and it is always one of a small number: a rate proportional to the amount present, a rate proportional to a difference of temperatures, a balance of what enters against what leaves, a balance of voltages around a loop, or mass times acceleration equal to the sum of forces.

The third stage translates the law into an equation. This is where most errors are made, because the translation requires a clear decision about signs and about which concentrations, temperatures or displacements appear.

The fourth stage solves the equation, using the methods for first-order separable equations, first-order linear equations, second-order linear equations with constant coefficients, and systems of linear equations with constant coefficients.

The fifth stage imposes the initial conditions and interprets the answer. Interpretation is not decoration: a question that asks when a population doubles, or what current survives after a long time, is answered by the interpreted solution and not by the formula alone.

> **Definition (State variable).** The state variable of a model is the quantity whose value at time $t$ determines the future of the model once the physical law is applied.

> **Definition (Initial value problem).** An initial value problem consists of a differential equation together with the values of the state variable and of enough of its derivatives at one instant to determine every constant in the general solution.

### 1.2 The law of natural growth and decay

> **Definition (Law of natural growth and decay).** A quantity obeys the law of natural growth when its rate of change is proportional to the amount present at that instant, so that
>
> $$
> \frac{dx}{dt}=kx ,
> $$
>
> where $x$ is the amount, $t$ is time, and $k$ is a constant of proportionality measured in reciprocal time. The law is called natural growth when $k>0$ and natural decay when $k<0$.

The phrase proportional to the amount present is the entire physical content. It says that a population of twice the size produces twice as many new individuals per unit time, that a sample of twice the mass emits twice as many particles per unit time, and that a bank balance of twice the size earns twice the interest per unit time. When a problem says that a rate is proportional to the amount present, the constant of proportionality is dimensionless in the sense that its unit is one over the unit of time.

The two quantities reported from this model are the doubling time and the half-life.

> **Definition (Doubling time and half-life).** For $k>0$, the doubling time is the time $T_{2}$ in which the amount doubles. For $k<0$, the half-life is the time $T_{1/2}$ in which the amount halves.

Both are independent of the starting amount, which is what makes them useful as fingerprints of a process. A radioactive isotope is identified by its half-life, and a bacterial culture is characterised by its doubling time.

The alternative and equally legitimate formulation uses a relative rate. Saying that a population grows by $2$ per cent per year means that after one year the population has been multiplied by $1.02$; the constant in the differential equation is then $\ln 1.02$, not $0.02$. The two descriptions agree to first order only, and the discrepancy is exactly what distinguishes a discrete annual percentage from a continuous relative rate.

### 1.3 Newton's law of cooling

> **Definition (Newton's law of cooling).** The temperature $T$ of a body in surroundings of temperature $T_{s}$ changes at a rate proportional to the excess of the body's temperature over the surroundings, so that
>
> $$
> \frac{dT}{dt}=-k\left(T-T_{s}\right) ,
> $$
>
> where $k>0$ is measured in reciprocal time and $T_{s}$ is held constant.

The law is empirical, and it is surprisingly accurate when the body is well mixed, when the surroundings are large compared with the body, and when the excess is modest. It is the same law in both directions: if the body starts colder than its surroundings the bracket is negative and the body warms, so no separate warming formula is needed.

The essential structural feature is that the rate refers to the excess, not to the temperature. A body at $90$ degrees in a room at $20$ degrees loses heat four times as fast as a body at $37.5$ degrees in the same room, because the excesses are $70$ and $17.5$ degrees. Nothing in the law refers to an absolute zero or to the outside world.

Its solution has a canonical form that is worth naming.

> **Definition (Exponential approach to equilibrium).** For constant $T_{s}$ and initial temperature $T_{0}$, the temperature is $T=T_{s}+\left(T_{0}-T_{s}\right)e^{-kt}$. The constant $T_{s}$ is the equilibrium temperature and the decaying term is the transient.

### 1.4 Conservation of mass in a well-stirred tank

> **Definition (Well-stirred tank).** A tank is well stirred when the concentration of dissolved substance is the same everywhere inside it at every instant, so that the liquid leaving has the same concentration as the liquid inside.

> **Definition (Concentration).** The concentration of a dissolved substance is the mass of the substance divided by the volume of solution, $c=Q/V$, measured in mass per unit volume.

With these two definitions the balance law becomes an equation.

> **Definition (Mixture balance law).** If brine of concentration $c_{in}$ enters a well-stirred tank at volume rate $r_{in}$ and the mixture leaves at volume rate $r_{out}$, then the mass $Q$ of dissolved substance satisfies
>
> $$
> \frac{dQ}{dt}=c_{in}r_{in}-\frac{Q}{V(t)}r_{out} ,
> $$
>
> where $V(t)$ is the volume of solution in the tank at time $t$.

Three features of this definition deserve emphasis.

The first is that both terms on the right are masses per unit time. The product $c_{in}r_{in}$ has units of mass per volume multiplied by volume per time, which is mass per time. The term $Qr_{out}/V$ has units of mass multiplied by volume per time divided by volume, which is again mass per time.

The second is that the concentration in the outgoing stream is $Q/V$, the concentration of the tank. It is not $c_{in}$, and using $c_{in}$ there is the classic error of the topic.

The third is that the volume is determined by a separate balance, the volume balance. Liquid enters at $r_{in}$ and leaves at $r_{out}$, so

$$
\frac{dV}{dt}=r_{in}-r_{out} ,
$$

and therefore $V(t)=V_{0}+\left(r_{in}-r_{out}\right)t$, where $V_{0}$ is the initial volume. When the two rates are equal the volume is constant and the equation for $Q$ has constant coefficients. When they differ the coefficient $r_{out}/V(t)$ varies with time and the equation needs an integrating factor.

### 1.5 Kirchhoff's voltage law and the element laws

> **Definition (Current and charge).** The current $i$, measured in amperes, is the rate at which charge passes a point of the circuit. The charge $q$, measured in coulombs, is the charge that has accumulated on the capacitor. They are related by $i=\frac{dq}{dt}$, and consequently $\frac{di}{dt}=\frac{d^{2}q}{dt^{2}}$.

> **Definition (Kirchhoff's voltage law).** Around any closed loop of a circuit, the sum of the voltage drops across the elements equals the electromotive force supplied to the loop.

The element laws supply the drops. Across a resistor the drop is $Ri$, which is Ohm's law. Across an inductor the drop is $L\frac{di}{dt}$, because a coil opposes change of current in proportion to the inductance. Across a capacitor the drop is $\frac{q}{C}$, because the voltage across a capacitor is proportional to the charge stored on it.

Combining the law with the element laws gives the two standard equations of the topic.

$$
L\frac{di}{dt}+Ri=E
$$

$$
L\frac{d^{2}q}{dt^{2}}+R\frac{dq}{dt}+\frac{q}{C}=E(t)
$$

The first is a first-order equation for the current in a circuit containing a coil and a resistor. The second is a second-order equation for the charge in a circuit containing all three elements, and it follows from the first by substituting $i=\frac{dq}{dt}$.

### 1.6 The vocabulary of the second-order circuit

The equation

$$
L\frac{d^{2}q}{dt^{2}}+R\frac{dq}{dt}+\frac{q}{C}=0
$$

is a linear homogeneous equation with constant coefficients, so its solutions are governed by the roots of the characteristic equation

$$
Lr^{2}+Rr+\frac{1}{C}=0 .
$$

> **Definition (Natural frequency and damping ratio).** For $L>0$ and $C>0$ the natural angular frequency is $\omega_{n}=\frac{1}{\sqrt{LC}}$, measured in radians per second, and the damping ratio is
>
> $$
> \zeta=\frac{R}{2}\sqrt{\frac{C}{L}} ,
> $$
>
> a pure number.

> **Definition (Classification).** The circuit is underdamped when $\zeta<1$, critically damped when $\zeta=1$ and overdamped when $\zeta>1$. Equivalently, with the discriminant $\Delta=R^{2}-\frac{4L}{C}$, it is underdamped when $\Delta<0$, critically damped when $\Delta=0$ and overdamped when $\Delta>0$. The resistance $R_{c}=2\sqrt{\frac{L}{C}}$ is the critical resistance.

> **Definition (Damped frequency).** In the underdamped case the charge oscillates with damped angular frequency $\omega_{d}=\omega_{n}\sqrt{1-\zeta^{2}}$, which may also be written $\omega_{d}=\sqrt{\frac{1}{LC}-\frac{R^{2}}{4L^{2}}}$.

The damping ratio is the single number that decides the qualitative behaviour, and the three cases produce three distinct solution shapes: a decaying oscillation, a single return with a possible linear factor, and a slow monotone return made of two exponentials.

### 1.7 Elastic springs and the two-mass system

> **Definition (Hooke's law).** A spring displaced from its natural length by an amount $s$ exerts a restoring force of magnitude $ks$, directed toward the natural length. The constant $k$ is the stiffness, measured in newtons per metre.

> **Definition (Equilibrium position).** The equilibrium position of a mass on a spring is the position at which the spring force balances every other force acting on the mass. Displacements are measured from this position, so that at equilibrium the displacement is zero.

Consider a smooth horizontal table with a fixed point $P$ at the left, a spring $S_{1}$ of stiffness $k_{1}$ joining $P$ to a mass $A_{1}$ of mass $m_{1}$, and a spring $S_{2}$ of stiffness $k_{2}$ joining $A_{1}$ to a mass $A_{2}$ of mass $m_{2}$. Let $x_{1}(t)$ and $x_{2}(t)$ be the displacements of the two masses to the right of their equilibrium positions, in metres.

> **Definition (Two-mass spring system).** With the notation above and no external forcing, the displacements satisfy
>
> $$
> m_{1}\frac{d^{2}x_{1}}{dt^{2}}=-\left(k_{1}+k_{2}\right)x_{1}+k_{2}x_{2} ,
> $$
>
> $$
> m_{2}\frac{d^{2}x_{2}}{dt^{2}}=k_{2}x_{1}-k_{2}x_{2} .
> $$

The equations are a system: neither can be solved without the other, because the acceleration of each mass depends on both displacements. Written in matrix form they become

$$
\begin{pmatrix} m_{1} & 0 \\ 0 & m_{2} \end{pmatrix}\begin{pmatrix} x_{1}'' \\ x_{2}'' \end{pmatrix}=\begin{pmatrix} -\left(k_{1}+k_{2}\right) & k_{2} \\ k_{2} & -k_{2} \end{pmatrix}\begin{pmatrix} x_{1} \\ x_{2} \end{pmatrix} ,
$$

which is the form in which the eigenvalue method applies.

### 1.8 Steady state, transient and time constant

> **Definition (Steady state and transient).** In a linear model with constant forcing, the steady state is the solution that does not change with time, and the transient is the remainder, which decays to zero.

For the tank with constant inflow concentration the steady state is $Q=c_{in}V$. For the inductive circuit it is $i=E/R$. For the capacitive circuit it is $q=CE$. For the forced second-order circuit it is $q=CE$ again, because at constant charge the derivatives vanish and the capacitor carries the whole supply voltage.

> **Definition (Time constant).** For a first-order linear equation with constant coefficients, the time constant is the reciprocal of the coefficient of the unknown after the coefficient of the derivative has been made one.

The inductive circuit has time constant $\frac{L}{R}$ and the capacitive circuit has time constant $RC$. Both are measured in seconds, and both have the same meaning: after one time constant the transient has fallen to $e^{-1}$, about $37$ per cent of its initial size, and after five time constants it has fallen below one per cent.

### 1.9 Initial conditions and the count of constants

The order of an equation fixes how many conditions are needed. A first-order model needs one condition, normally the value of the state variable at $t=0$: the initial population, the initial temperature, the initial mass of salt, the initial current, or the initial charge. A second-order model needs two, normally the value and its derivative at $t=0$: the initial charge and the initial current, or the initial displacements and the initial velocities. A system of two second-order equations needs four.

Two conventions matter when the conditions are imposed. The first is that unless a problem says otherwise, the switch is closed at $t=0$ and time is measured from that instant. The second is that a body released from rest has zero velocity, so the derivative of every displacement vanishes at $t=0$; a circuit with an open switch carries no current before closing, so the initial current is zero even when the initial charge is not.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The exponential law

> **Theorem (Natural growth and decay).** Let $k$ be a real constant and let $x$ be a positive differentiable function satisfying $\frac{dx}{dt}=kx$ on an interval containing $0$. Then $x(t)=x(0)e^{kt}$ on that interval, and conversely every function of that form satisfies the equation.

The converse half is verified by differentiation and is the check always performed at the end of a solution. The direct half is proved in Section 3.1. Two consequences are used constantly.

> **Corollary (Scale invariance).** If $x$ satisfies the growth law then so does every constant multiple of $x$, and the ratio $x(t)/x(s)$ depends only on the difference $t-s$.

Scale invariance is the mathematical statement that the doubling time does not depend on the starting amount, because

$$
\frac{x(t+T_{2})}{x(t)}=e^{kT_{2}} ,
$$

and the right-hand side contains no $t$. This is a strong and slightly counter-intuitive property: an exponentially growing population adds more individuals each year than the year before, yet takes the same time to double at every stage.

> **Corollary (Doubling time and half-life).** If $k>0$ then $T_{2}=\frac{\ln 2}{k}$. If $k<0$ then $T_{1/2}=\frac{\ln 2}{|k|}$.

> **Lemma (Uniqueness).** Two solutions of $\frac{dx}{dt}=kx$ that agree at one instant agree everywhere.

The lemma, a special case of the Picard–Lindelöf theorem, is what licenses the practice of writing down the solution from the initial value alone. It also justifies the habit of fitting $k$ from a single later observation: one observation plus the starting value determine the unique solution through both.

### 2.2 The cooling theorem

> **Theorem (Newton's law of cooling).** If $T_{s}$ is constant and $T$ satisfies $\frac{dT}{dt}=-k\left(T-T_{s}\right)$ with $T(0)=T_{0}$, then
>
> $$
> T(t)=T_{s}+\left(T_{0}-T_{s}\right)e^{-kt} .
> $$

> **Lemma (Translation).** Replacing $T$ by the excess $u=T-T_{s}$ converts Newton's law of cooling into the natural decay law $\frac{du}{dt}=-ku$.

The lemma explains why cooling problems are no harder than decay problems: they are the same problem measured from a different origin. It also shows the correct convention for a body colder than its surroundings. If $T_{0}<T_{s}$ then $u_{0}<0$ and $u$ decays toward zero from below, so $T$ rises toward $T_{s}$. The single formula covers warming and cooling.

> **Corollary (Monotonicity and confinement).** A solution of the cooling law is strictly monotone and never crosses $T_{s}$. It approaches $T_{s}$ as $t\to\infty$ but attains it at no finite time.

### 2.3 The mixture theorems

> **Theorem (Constant-volume tank).** Suppose $r_{in}=r_{out}=r$ and $c_{in}$ is constant. Then $V$ is constant, and the solution of the balance law with $Q(0)=Q_{0}$ is
>
> $$
> Q(t)=c_{in}V+\left(Q_{0}-c_{in}V\right)e^{-rt/V} .
> $$

The theorem has an immediate interpretation. The steady state is $c_{in}V$, the mass the tank would contain if filled with incoming brine, and the transient is the initial deviation from that state, decaying at the rate $r/V$. The ratio $V/r$ is a time constant measured in the unit of time, since volume divided by volume per time is time.

> **Corollary (Limit and monotonicity).** With the hypotheses of the theorem, $Q(t)\to c_{in}V$ as $t\to\infty$, the concentration tends to $c_{in}$, and $Q$ is monotone, increasing when $Q_{0}<c_{in}V$ and decreasing when $Q_{0}>c_{in}V$.

> **Theorem (Variable-volume tank).** Suppose $r_{in}\neq r_{out}$, so that $V(t)=V_{0}+\mu t$ with $\mu=r_{in}-r_{out}$. Then
>
> $$
> Q(t)=c_{in}V(t)+C\left(V(t)\right)^{-r_{out}/\mu} ,
> $$
>
> where $C$ is determined by the initial mass.

The second term is the transient and it is no longer a pure exponential when $\mu\neq0$, because the volume changes. The steady-state term is still $c_{in}V(t)$, which is now a moving target: the mass the tank would hold if it were at the strength of the inflow at that instant.

> **Corollary (Draining and filling).** If the tank drains, so that $r_{out}>r_{in}$ and $\mu<0$, the volume reaches zero at $t=-\frac{V_{0}}{\mu}$ and the model ceases to apply there; the concentration tends to $c_{in}$ as the tank empties. If the tank fills, the volume grows without bound and the concentration again tends to $c_{in}$.

### 2.4 The first-order circuit theorems

> **Theorem (Linear circuit with constant coefficients).** The solution of $L\frac{di}{dt}+Ri=E(t)$ with $i(0)=i_{0}$ is
>
> $$
> i(t)=e^{-Rt/L}\left(i_{0}+\frac{1}{L}\int_{0}^{t}E(s)e^{Rs/L}\,ds\right) .
> $$

For constant $E$ the integral evaluates and the solution reduces to the familiar form.

> **Corollary (Inductive circuit).** For constant $E$, $i(t)=\frac{E}{R}+\left(i_{0}-\frac{E}{R}\right)e^{-Rt/L}$. The current tends to $\frac{E}{R}$ and the time constant is $\frac{L}{R}$.

> **Corollary (Capacitive circuit).** For $R\frac{dq}{dt}+\frac{q}{C}=E$ with constant $E$ and $q(0)=q_{0}$,
>
> $$
> q(t)=CE+\left(q_{0}-CE\right)e^{-t/(RC)} , \qquad i(t)=\frac{E-\frac{q_{0}}{C}}{R}e^{-t/(RC)} .
> $$

> **Lemma (Five time constants).** After five time constants the transient has fallen to $e^{-5}$, which is less than $0.007$ of its original size, so the circuit is for practical purposes in its steady state.

The five-time-constant rule is the standard justification for calling $\frac{E}{R}$ the steady current or the steady charge. It also tells the student how much of the time axis is worth plotting: a graph over ten time constants shows everything.

> **Lemma (Sinusoidal forcing).** For $E=E_{0}\sin\omega t$ the particular integral is $\frac{E_{0}}{Z}\sin\left(\omega t-\varphi\right)$ with $Z=\sqrt{R^{2}+\omega^{2}L^{2}}$ and $\tan\varphi=\frac{\omega L}{R}$.

The quantity $Z$ is the impedance of the coil and resistor in series, and the phase lag $\varphi$ is the amount by which the current trails the applied voltage. The transient remains an exponential with the same time constant as before; only the steady state changes.

### 2.5 The classification theorem for the second-order circuit

> **Theorem (RLC classification).** Consider $Lq''+Rq'+q/C=0$ with $L,R,C>0$ and write $\Delta=R^{2}-\frac{4L}{C}$. The characteristic roots are
>
> $$
> r_{1},r_{2}=\frac{-R\pm\sqrt{\Delta}}{2L} .
> $$
>
> If $\Delta<0$ the general solution is $q=e^{-Rt/(2L)}\left(A\cos\omega_{d}t+B\sin\omega_{d}t\right)$ with $\omega_{d}=\sqrt{\frac{1}{LC}-\frac{R^{2}}{4L^{2}}}$. If $\Delta=0$ the general solution is $q=\left(A+Bt\right)e^{-Rt/(2L)}$. If $\Delta>0$ the general solution is $q=Ae^{r_{1}t}+Be^{r_{2}t}$ with both roots real and negative.

Three observations make the theorem usable without memorising it.

The first is that the sign of $\Delta$ is the sign of $R^{2}C-4L$ after multiplying by $C$, so the comparison is between the resistance squared and four times the inductance over the capacitance. The threshold is the critical resistance $R_{c}=2\sqrt{L/C}$.

The second is that both roots have negative real part whenever $R>0$, because their sum is $-\frac{R}{L}$ and their product is $\frac{1}{LC}$, which is positive. Every solution therefore decays. In the underdamped case the envelope decays at the rate $\frac{R}{2L}$; in the overdamped case the slower of the two roots governs the late behaviour, which is why a large resistance makes the return sluggish.

The third is the ordering of the return speeds. For small resistance the charge oscillates and settles quickly. At critical damping it returns as fast as possible without oscillating. Beyond critical damping one root becomes very small in size, so part of the charge decays slowly and the return is sluggish.

> **Lemma (Critical damping minimises the settling time among non-oscillating cases).** Among all choices of $R$ with $L$ and $C$ fixed that do not produce an oscillation, the critically damped case returns the charge to zero fastest.

> **Lemma (Energy).** For the homogeneous circuit the stored energy $U=\frac{1}{2}Lq'^{2}+\frac{q^{2}}{2C}$ satisfies $\frac{dU}{dt}=-Rq'^{2}$, so the energy decreases whenever current flows and is dissipated entirely in the resistance.

The energy identity explains the classification physically. With no resistance no energy is lost and the charge oscillates forever. With resistance the energy drains away, and whether the charge swings through zero on the way depends on whether the resistor removes the energy faster than the oscillation can turn it around.

### 2.6 The spring system as an eigenvalue problem

> **Theorem (Normal modes).** The system $Mx''=Kx$ with $M$ diagonal positive and $K$ symmetric negative definite has a general solution that is a sum of two normal modes, each of the form $\left(\text{vector}\right)\cos\left(\omega t-\delta\right)$, where $\omega^{2}$ is an eigenvalue of $-M^{-1}K$ taken with a sign that makes it positive.

> **Lemma (Trace and determinant checks).** For the two-mass system with matrix $A=M^{-1}K$,
>
> $$
> \lambda_{1}+\lambda_{2}=-\frac{k_{1}+k_{2}}{m_{1}}-\frac{k_{2}}{m_{2}} , \qquad \lambda_{1}\lambda_{2}=\frac{k_{1}k_{2}}{m_{1}m_{2}} .
> $$

These two identities are the fastest available check on an eigenvalue computation, since they use only the physical constants.

> **Corollary (Symmetric case).** If $m_{1}=m_{2}=m$ and $k_{1}=k_{2}=k$ then the eigenvalues of $A$ are $\frac{k}{m}\cdot\frac{-3\pm\sqrt{5}}{2}$, so the normal frequencies are $\sqrt{\frac{k}{m}\cdot\frac{3\mp\sqrt{5}}{2}}$.

In the symmetric case the two modes have a definite character. The lower frequency mode has the masses moving in the same direction, the higher frequency mode has them moving in opposite directions. For the course numbers $m=1$, $k_{1}=3$, $k_{2}=2$ the eigenvalues are exactly $-1$ and $-6$, so the frequencies are $1$ and $\sqrt{6}$ radians per second, and the corresponding amplitude ratios are $1$ to $2$ and $2$ to $-1$.

### 2.7 Superposition and the structure of forced solutions

> **Theorem (Superposition).** If $q_{h}$ satisfies the homogeneous equation and $q_{p}$ satisfies the equation with right-hand side $E(t)$, then $q_{h}+q_{p}$ satisfies the equation with right-hand side $E(t)$.

The theorem is what allows the work in a forced circuit to be split into a complementary function and a particular integral. In the constant-forcing case the particular integral is the constant $CE$, which is the steady charge, and the complementary function is the transient determined by the initial conditions. Every forced problem in this topic is solved in that order: steady state first, transient second, constants last.

> **Lemma (Insensitivity of the transient to constant forcing).** Adding a constant to $E$ changes the steady state but not the decay rate of the transient.

The lemma is a consequence of the fact that the homogeneous equation is unaffected by the right-hand side. It explains why the time constant of a circuit can be quoted without knowing the battery voltage.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Deriving the exponential law from the proportional-rate hypothesis

The hypothesis is that the rate is $k$ times the amount. That is already the equation; what must be derived is its solution.

Step 1. Separate the variables on any interval where $x$ does not vanish.

$$
\frac{1}{x}\frac{dx}{dt}=k
$$

Step 2. Integrate both sides with respect to $t$.

$$
\int\frac{1}{x}\frac{dx}{dt}\,dt=\int k\,dt
$$

Step 3. Change the variable on the left, using $\frac{dx}{dt}dt=dx$, and integrate.

$$
\ln\left|x\right|=kt+C
$$

Step 4. Exponentiate. Writing $e^{C}$ as the positive constant $A$ and allowing the sign to be absorbed, the solution is $x=Ae^{kt}$.

Step 5. Impose $x(0)=x_{0}$, which gives $A=x_{0}$ because $e^{0}=1$.

$$
x=x_{0}e^{kt}
$$

Step 6. Verify by differentiating and by evaluating at zero. Both hold, and by the uniqueness lemma of Section 2.1 this is the only solution with that initial value.

The step that is most often written carelessly is the change of variable in Step 3. It is valid because both sides are integrals with respect to the same variable, and because the left side is the derivative of $\ln\left|x\right|$ composed with $x(t)$; it is not valid because $dx$ and $dt$ are numbers that may be separated at will.

### 3.2 Deriving the cooling solution

Step 1. Define the excess $u=T-T_{s}$. Since $T_{s}$ is constant, $\frac{du}{dt}=\frac{dT}{dt}$.

Step 2. Substitute into Newton's law.

$$
\frac{du}{dt}=-k\left(T-T_{s}\right)=-ku
$$

Step 3. Apply the exponential law of Section 3.1 with the constant $-k$.

$$
u=u_{0}e^{-kt}
$$

Step 4. Translate back, using $u_{0}=T_{0}-T_{s}$.

$$
T=T_{s}+\left(T_{0}-T_{s}\right)e^{-kt}
$$

Step 5. Verify. Differentiating gives $-k\left(T_{0}-T_{s}\right)e^{-kt}$, which is $-ku=-k\left(T-T_{s}\right)$, and at $t=0$ the formula returns $T_{0}$.

The derivation shows that the constant $k$ is not the rate of cooling; it is the rate of cooling per degree of excess. A body whose excess is twice as large cools twice as fast, which is the physical content of the law.

### 3.3 Deriving the mixture equation and solving it

The modelling step is a statement of conservation of mass applied to the dissolved substance.

Step 1. In a short interval of time from $t$ to $t+h$, the mass entering is $c_{in}r_{in}h$ and the mass leaving is $c_{out}(t)r_{out}h$, where $c_{out}(t)$ is the concentration of the outgoing liquid.

Step 2. The change in the mass in the tank is the net inflow.

$$
Q(t+h)-Q(t)=c_{in}r_{in}h-c_{out}(t)r_{out}h
$$

Step 3. Divide by $h$ and let $h\to0$. Since the tank is well stirred, the outgoing concentration equals the tank concentration $Q(t)/V(t)$ at every instant.

$$
\frac{dQ}{dt}=c_{in}r_{in}-\frac{Q}{V}r_{out}
$$

This is the step at which the concentration must be expressed correctly. The outflow carries the tank's concentration, and the tank's concentration is $Q/V$; substituting $c_{in}$ there would describe a tank whose outflow is independent of its contents, which is not a tank at all.

Step 4. Supply the volume from the volume balance. Liquid is incompressible, so the volume changes at the net volume rate.

$$
\frac{dV}{dt}=r_{in}-r_{out} , \qquad V(t)=V_{0}+\left(r_{in}-r_{out}\right)t
$$

Step 5. Solve the constant-volume case, in which $r_{in}=r_{out}=r$ and $V$ is constant. The equation is linear with constant coefficients, and its integrating factor is $e^{rt/V}$.

$$
\frac{d}{dt}\left(Qe^{rt/V}\right)=c_{in}re^{rt/V}
$$

Step 6. Integrate and divide by the integrating factor.

$$
Q=c_{in}V+Ce^{-rt/V}
$$

Step 7. Impose $Q(0)=Q_{0}$, which gives $C=Q_{0}-c_{in}V$, so

$$
Q=c_{in}V+\left(Q_{0}-c_{in}V\right)e^{-rt/V} .
$$

Step 8. Solve the general case by the integrating factor $V^{r_{out}/\mu}$, where $\mu=r_{in}-r_{out}$. Because $\frac{dV}{dt}=\mu$,

$$
\frac{d}{dt}\left(QV^{r_{out}/\mu}\right)=c_{in}r_{in}V^{r_{out}/\mu} .
$$

Step 9. Integrate with respect to $t$, using $dt=\frac{dV}{\mu}$ and noting that $r_{out}+\mu=r_{in}$.

$$
QV^{r_{out}/\mu}=c_{in}V^{1+r_{out}/\mu}+C
$$

Step 10. Divide by $V^{r_{out}/\mu}$ to obtain the general solution of Section 2.3.

$$
Q=c_{in}V+CV^{-r_{out}/\mu}
$$

Step 11. Verify by differentiation. Writing $m=r_{out}/\mu$, the derivative is $c_{in}\mu-CmV^{-m-1}\mu=c_{in}\mu-Cr_{out}V^{-m-1}$, while the right-hand side of the balance law is $c_{in}r_{in}-r_{out}V^{-1}\left(c_{in}V+CV^{-m}\right)=c_{in}\mu-Cr_{out}V^{-m-1}$. The two agree, so the solution is correct for every choice of $C$.

### 3.4 Deriving the inductive-circuit equation and its solution

Step 1. Apply Kirchhoff's voltage law to the loop containing the battery, the resistor and the coil. The drops are $Ri$ and $L\frac{di}{dt}$, and their sum is the supply.

$$
L\frac{di}{dt}+Ri=E
$$

Step 2. Divide by $L$ so that the coefficient of the derivative is one, and identify the integrating factor $e^{Rt/L}$.

Step 3. Multiply through and collapse the left side.

$$
\frac{d}{dt}\left(ie^{Rt/L}\right)=\frac{E}{L}e^{Rt/L}
$$

Step 4. Integrate from $0$ to $t$, which automatically builds in the initial current.

$$
i(t)e^{Rt/L}-i_{0}=\frac{1}{L}\int_{0}^{t}E(s)e^{Rs/L}\,ds
$$

Step 5. Solve for $i$.

$$
i(t)=i_{0}e^{-Rt/L}+\frac{1}{L}\int_{0}^{t}E(s)e^{-R(t-s)/L}\,ds
$$

Step 6. For constant $E$ evaluate the integral to obtain $i=\frac{E}{R}+\left(i_{0}-\frac{E}{R}\right)e^{-Rt/L}$.

Step 7. For sinusoidal $E=E_{0}\sin\omega t$ seek a particular integral $i_{p}=A\sin\omega t+B\cos\omega t$ and match coefficients.

$$
LA\omega\cos\omega t-LB\omega\sin\omega t+RA\sin\omega t+RB\cos\omega t=E_{0}\sin\omega t
$$

Step 8. Equate the coefficients of the cosine and the sine.

$$
LA\omega+RB=0 , \qquad RA-LB\omega=E_{0}
$$

Step 9. Solve the pair.

$$
A=\frac{E_{0}R}{R^{2}+\omega^{2}L^{2}} , \qquad B=-\frac{E_{0}\omega L}{R^{2}+\omega^{2}L^{2}}
$$

Step 10. Combine the two terms into a single sine with a phase lag, using $Z=\sqrt{R^{2}+\omega^{2}L^{2}}$.

$$
i_{p}=\frac{E_{0}}{Z}\sin\left(\omega t-\varphi\right) , \qquad \tan\varphi=\frac{\omega L}{R}
$$

Step 11. Verify the particular integral by substitution, and add the transient $\frac{E_{0}\omega L}{R^{2}+\omega^{2}L^{2}}e^{-Rt/L}$ chosen so that the initial current is zero.

The verification in Step 11 is worth doing explicitly once. With $i=2\sin 40t-4\cos 40t$, $R=10$, $L=0.5$ and $E=100\sin 40t$, the left side is $0.5\left(80\cos 40t+160\sin 40t\right)+10\left(2\sin 40t-4\cos 40t\right)$, which is $100\sin 40t$ after the cosines cancel.

### 3.5 Deriving the capacitive-circuit equation

Step 1. Apply Kirchhoff's law to a loop containing the battery, the resistor and the capacitor. The capacitor's drop is $q/C$.

$$
R\frac{dq}{dt}+\frac{q}{C}=E
$$

Step 2. Divide by $R$, giving $\frac{dq}{dt}+\frac{q}{RC}=\frac{E}{R}$, with time constant $RC$.

Step 3. Solve as in Section 3.4 with $p=\frac{1}{RC}$ and constant right side.

$$
q=CE+\left(q_{0}-CE\right)e^{-t/(RC)}
$$

Step 4. Differentiate to obtain the current, using $i=\frac{dq}{dt}$.

$$
i=\frac{E-\frac{q_{0}}{C}}{R}e^{-t/(RC)}
$$

Step 5. Interpret and verify. The final charge is $CE$, the initial current is $\frac{E}{R}-\frac{q_{0}}{RC}$, which is the supply minus the capacitor's initial voltage, all divided by the resistance. Substituting $q$ and its derivative back into the loop equation returns $E$ identically.

The resemblance to the inductive circuit is exact once the roles are assigned: charge replaces current, capacitance replaces inductance, and $RC$ replaces $L/R$. The two circuits are electrical duals.

### 3.6 Deriving the second-order circuit equation and its classification

Step 1. Apply Kirchhoff's law to the loop containing the battery, the resistor, the coil and the capacitor.

$$
L\frac{di}{dt}+Ri+\frac{q}{C}=E(t)
$$

Step 2. Use the definition of current as the rate of change of charge, $i=\frac{dq}{dt}$, and hence $\frac{di}{dt}=\frac{d^{2}q}{dt^{2}}$.

$$
L\frac{d^{2}q}{dt^{2}}+R\frac{dq}{dt}+\frac{q}{C}=E(t)
$$

Step 3. For the homogeneous case set $E=0$ and substitute the trial solution $q=e^{rt}$.

$$
\left(Lr^{2}+Rr+\frac{1}{C}\right)e^{rt}=0
$$

Step 4. Since an exponential never vanishes, the bracket must vanish. This is the characteristic equation, and its roots are found by the quadratic formula.

$$
r=\frac{-R\pm\sqrt{R^{2}-\frac{4L}{C}}}{2L}
$$

Step 5. Read the classification from the discriminant $\Delta=R^{2}-\frac{4L}{C}$. When $\Delta<0$ the roots are a complex conjugate pair with real part $-\frac{R}{2L}$ and imaginary part $\pm\sqrt{\frac{1}{LC}-\frac{R^{2}}{4L^{2}}}$, which is the damped frequency. When $\Delta=0$ the roots coincide at $-\frac{R}{2L}$ and the second solution is $t$ times the exponential. When $\Delta>0$ the roots are real and both are negative, because their product is $\frac{1}{LC}>0$ and their sum is $-\frac{R}{L}<0$.

Step 6. Express the boundary in the two standard ways. Setting $\Delta=0$ gives $R_{c}=2\sqrt{\frac{L}{C}}$, and dividing $R$ by $R_{c}$ gives the damping ratio $\zeta=\frac{R}{2}\sqrt{\frac{C}{L}}$.

Step 7. Prove the energy identity. With $U=\frac{1}{2}L\left(q'\right)^{2}+\frac{q^{2}}{2C}$,

$$
\frac{dU}{dt}=Lq'q''+\frac{qq'}{C}=q'\left(Lq''+\frac{q}{C}\right)=-R\left(q'\right)^{2} ,
$$

which is negative whenever the current is non-zero.

Step 8. Verify a representative solution. For $L=1$, $R=2$, $C=\frac{1}{5}$ the equation is $q''+2q'+5q=0$ and the proposed solution $q=e^{-t}\left(0.01\cos 2t+0.005\sin 2t\right)$ has $q(0)=0.01$ and $q'(0)=0$; differentiating twice and substituting confirms that the combination vanishes identically.

### 3.7 Deriving the two-mass spring system

Step 1. Choose coordinates. Let $x_{1}$ and $x_{2}$ be displacements to the right of the equilibrium positions, so the extension of the first spring is $x_{1}$ and the extension of the second spring is $x_{2}-x_{1}$.

Step 2. Apply Hooke's law to each spring. The first spring pulls $A_{1}$ to the left with force $k_{1}x_{1}$. The second spring, stretched by $x_{2}-x_{1}$, pulls $A_{1}$ to the right with force $k_{2}\left(x_{2}-x_{1}\right)$ and pulls $A_{2}$ to the left with the same force.

Step 3. Apply Newton's second law to each mass.

$$
m_{1}\frac{d^{2}x_{1}}{dt^{2}}=-k_{1}x_{1}+k_{2}\left(x_{2}-x_{1}\right)
$$

$$
m_{2}\frac{d^{2}x_{2}}{dt^{2}}=-k_{2}\left(x_{2}-x_{1}\right)
$$

Step 4. Collect the terms into the standard symmetric form.

$$
m_{1}x_{1}''+\left(k_{1}+k_{2}\right)x_{1}-k_{2}x_{2}=0
$$

$$
m_{2}x_{2}''-k_{2}x_{1}+k_{2}x_{2}=0
$$

Step 5. Write the system in matrix form $Mx''=Kx$ and multiply by $M^{-1}$.

$$
x''=Ax , \qquad A=\begin{pmatrix} -\frac{k_{1}+k_{2}}{m_{1}} & \frac{k_{2}}{m_{1}} \\ \frac{k_{2}}{m_{2}} & -\frac{k_{2}}{m_{2}} \end{pmatrix}
$$

Step 6. Seek a normal mode $x=ve^{\omega t}$ with $v$ a constant vector. Substitution gives $\omega^{2}v=Av$, so $\omega^{2}$ must be an eigenvalue of $A$ and $v$ an eigenvector.

Step 7. Compute the characteristic polynomial of $A$ and check it against the trace and determinant identities of Section 2.6.

$$
\lambda^{2}+\left(\frac{k_{1}+k_{2}}{m_{1}}+\frac{k_{2}}{m_{2}}\right)\lambda+\frac{k_{1}k_{2}}{m_{1}m_{2}}=0
$$

Step 8. Since the coefficients are positive and the constant is positive, both roots are negative; write them as $-\omega_{1}^{2}$ and $-\omega_{2}^{2}$.

Step 9. Write the general solution as a combination of the two modes, each with its own phase.

$$
x=a_{1}v_{1}\cos\left(\omega_{1}t\right)+b_{1}v_{1}\sin\left(\omega_{1}t\right)+a_{2}v_{2}\cos\left(\omega_{2}t\right)+b_{2}v_{2}\sin\left(\omega_{2}t\right)
$$

Step 10. Impose the four initial conditions to determine $a_{1}$, $b_{1}$, $a_{2}$ and $b_{2}$, and verify by substituting one mode back into both original equations.

The whole method is thus an eigenvalue problem wearing physical clothes. The eigenvalues supply the two allowed frequencies, the eigenvectors supply the two allowed shapes of motion, and the four initial conditions supply the amounts of each shape.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: radiometric decay of a sample

A radioactive element decays at a rate proportional to the amount present, and half of an initial sample disappears in $1600$ years. Find the decay constant exactly, the percentage lost in $100$ years, and the time for only one tenth of the original amount to remain.

### 4.2 Solution: fit the half-life, then substitute twice

Step 1. Name the quantities and write the law. Let $x$ be the mass present after $t$ years and let $k>0$ be the decay constant in reciprocal years.

$$
\frac{dx}{dt}=-kx
$$

Step 2. Write the solution with the initial mass $x_{0}$.

$$
x=x_{0}e^{-kt}
$$

Step 3. Use the half-life to determine $k$. At $t=1600$ the mass is $\frac{x_{0}}{2}$.

$$
\frac{1}{2}=e^{-1600k}
$$

$$
k=\frac{\ln 2}{1600}=4.3322\times10^{-4}
$$

Step 4. Compute the fraction remaining after $100$ years.

$$
\frac{x}{x_{0}}=e^{-4.3322\times10^{-4}\times100}=e^{-0.043322}=0.95759
$$

Step 5. Convert the fraction remaining to a percentage lost.

$$
\left(1-0.95759\right)\times100=4.24
$$

So $4.24$ per cent is lost in the first century.

Step 6. Solve for the time at which one tenth remains.

$$
0.1=e^{-kt}
$$

$$
t=\frac{\ln 10}{k}=\frac{2.302585}{4.3322\times10^{-4}}=5315
$$

Step 7. Interpret. One tenth remains after about $5315$ years, which is a little more than three half-lives, as it must be, since three half-lives leave one eighth and four leave one sixteenth.

Step 8. Check. Substitute $t=1600$ into the solution to recover one half, and differentiate the solution to recover the decay law.

### 4.3 Problem: coffee cooling in a room

Coffee at $90$ degrees Celsius is left in a room at $20$ degrees, and after $10$ minutes it is at $60$ degrees. Find the temperature after $30$ minutes and the time at which it reaches $30$ degrees.

### 4.4 Solution: reduce to the excess and fit one constant

Step 1. Write Newton's law of cooling with $T_{s}=20$.

$$
\frac{dT}{dt}=-k\left(T-20\right)
$$

Step 2. Write the solution with $T_{0}=90$.

$$
T=20+70e^{-kt}
$$

Step 3. Impose the observation at $t=10$. The excess there is $40$ degrees.

$$
40=70e^{-10k}
$$

$$
e^{-10k}=\frac{4}{7} , \qquad k=\frac{1}{10}\ln\frac{7}{4}=0.055962
$$

Step 4. Compute the temperature at $t=30$. Since thirty minutes is three lots of ten, the exponential is the cube of four sevenths.

$$
T=20+70\left(\frac{4}{7}\right)^{3}=20+70\times0.18659=20+13.06=33.1
$$

Step 5. Solve for the time at which the excess is $10$ degrees.

$$
10=70e^{-kt}
$$

$$
t=\frac{\ln 7}{k}=\frac{1.945910}{0.055962}=34.8
$$

Step 6. Interpret. The coffee is at about $33$ degrees after half an hour and reaches $30$ degrees after about $34.8$ minutes. The excess halves every $\frac{\ln 2}{k}=12.4$ minutes.

Step 7. Check. At $t=0$ the formula gives $90$, at $t=10$ it gives $20+40=60$, and the derivative at $t=0$ is $-k\times70=-3.92$ degrees per minute, so the coffee cools fastest when the excess is largest, as the law requires.

### 4.5 Problem: a tank with equal inflow and outflow

A tank holds $400$ litres of fresh water. Brine containing $0.05$ kilograms of salt per litre enters at $6$ litres per minute, and the well-stirred mixture leaves at the same rate. Find the mass of salt at time $t$, the mass after $100$ minutes, and the time at which $10$ kilograms has accumulated.

### 4.6 Solution: balance the rates and use the constant-volume formula

Step 1. Name the unknown. Let $Q$ be the mass of salt in kilograms at time $t$ in minutes.

Step 2. Compute the entry rate and the exit rate. The entry rate is $0.05\times6=0.3$ kilograms per minute. The exit rate is $6$ times the tank concentration $Q/400$, that is $0.015Q$ kilograms per minute.

Step 3. Write the balance law with the initial condition.

$$
\frac{dQ}{dt}=0.3-0.015Q , \qquad Q(0)=0
$$

Step 4. Identify the steady state by setting the derivative to zero, and read off the time constant.

$$
Q_{\infty}=\frac{0.3}{0.015}=20 , \qquad \frac{1}{0.015}=66.67 \text{ minutes}
$$

Step 5. Apply the formula of Section 2.3 with $Q_{0}=0$.

$$
Q=20\left(1-e^{-0.015t}\right)
$$

Step 6. Evaluate at $t=100$. The exponential is $e^{-1.5}=0.22313$.

$$
Q=20\left(1-0.22313\right)=20\times0.77687=15.54
$$

Step 7. Solve for the time at which $Q=10$.

$$
10=20\left(1-e^{-0.015t}\right) , \qquad e^{-0.015t}=\frac{1}{2}
$$

$$
t=\frac{\ln 2}{0.015}=46.2
$$

Step 8. Check and interpret. The derivative of the answer is $0.3e^{-0.015t}$, while the right side of the balance law is $0.3-0.015\times20\left(1-e^{-0.015t}\right)=0.3e^{-0.015t}$, so the equation holds; the initial mass is zero; the mass rises monotonically to the steady value $20$ kilograms, at which the tank is exactly as strong as the incoming brine.

### 4.7 Problem: a tank that drains while being fed

A tank contains $100$ litres of brine with $5$ kilograms of salt dissolved. Brine of concentration $0.02$ kilograms per litre enters at $4$ litres per minute, and the well-stirred mixture leaves at $5$ litres per minute. Find the mass of salt at time $t$ and the concentration when $10$ litres remain.

### 4.8 Solution: the volume falls, so the coefficient is not constant

Step 1. Name the unknown and write the volume balance.

$$
V(t)=100+\left(4-5\right)t=100-t
$$

Step 2. Write the balance law with the concentration expressed as $Q/V$.

$$
\frac{dQ}{dt}=0.02\times4-\frac{Q}{100-t}\times5=0.08-\frac{5Q}{100-t}
$$

Step 3. Put the equation in standard linear form and identify the integrating factor. With $\mu=4-5=-1$ and $r_{out}=5$ the exponent $r_{out}/\mu$ is $-5$, so the integrating factor is $V^{-5}$.

$$
\frac{d}{dt}\left(Q\left(100-t\right)^{-5}\right)=0.08\left(100-t\right)^{-5}
$$

Step 4. Integrate. Since the derivative of $\left(100-t\right)^{-4}$ is $4\left(100-t\right)^{-5}$,

$$
Q\left(100-t\right)^{-5}=0.02\left(100-t\right)^{-4}+C
$$

Step 5. Multiply by $\left(100-t\right)^{5}$.

$$
Q=0.02\left(100-t\right)+C\left(100-t\right)^{5}
$$

Step 6. Impose $Q(0)=5$.

$$
5=2+100^{5}C , \qquad C=\frac{3}{10^{10}}
$$

Step 7. State the solution and evaluate when $10$ litres remain, that is at $t=90$.

$$
Q=0.02\left(100-t\right)+3\times10^{-10}\left(100-t\right)^{5}
$$

$$
Q(90)=0.2+3\times10^{-10}\times10^{5}=0.20003
$$

Step 8. Compute the concentration.

$$
c=\frac{Q}{V}=\frac{0.20003}{10}=0.0200
$$

Step 9. Check and interpret. At $t=0$ the formula gives $2+3=5$ kilograms; differentiating at $t=0$ gives $-0.02-0.15=-0.17$, while the balance law gives $0.08-5\times5/100=-0.17$, so the equation holds. The concentration has fallen to the strength of the inflow, as it must: the tank is being flushed with brine of that strength and the salt it started with has almost all washed out.

### 4.9 Problem: a coil of inductance switched onto a battery

A circuit in series has a battery of $24$ volts, a resistance of $6$ ohms and an inductance of $0.5$ henries. At $t=0$ the switch is closed and the current is zero. Find the current at time $t$, the current at $t=0.1$ seconds, and the steady current.

### 4.10 Solution: divide by the inductance and read the time constant

Step 1. Write Kirchhoff's law for the loop.

$$
0.5\frac{di}{dt}+6i=24
$$

Step 2. Divide through by $0.5$.

$$
\frac{di}{dt}+12i=48
$$

Step 3. Identify the steady current and the time constant.

$$
i_{\infty}=\frac{48}{12}=4 , \qquad \frac{L}{R}=\frac{1}{12}=0.0833 \text{ s}
$$

Step 4. Write the solution with $i(0)=0$.

$$
i=4\left(1-e^{-12t}\right)
$$

Step 5. Evaluate at $t=0.1$. The exponent is $1.2$.

$$
i=4\left(1-0.30119\right)=2.80
$$

Step 6. Check. The derivative is $48e^{-12t}$, so $0.5\times48e^{-12t}+6\times4\left(1-e^{-12t}\right)=24e^{-12t}+24-24e^{-12t}=24$, which is the battery voltage. The initial current is zero and the current rises toward $4$ amperes without overshooting, because the right side is positive for every $i<4$ and negative for every $i>4$.

### 4.11 Problem: charging a capacitor

A circuit in series has a battery of $100$ volts, a resistance of $10$ ohms and a capacitance of $2\times10^{-4}$ farads. The capacitor is uncharged when the switch is closed. Find the charge and the current at time $t$, and their values at $t=0.002$ seconds.

### 4.12 Solution: the capacitive drop is the charge over the capacitance

Step 1. Write Kirchhoff's law with the capacitor's drop equal to $q$ divided by $2\times10^{-4}$, that is $5000q$.

$$
10\frac{dq}{dt}+5000q=100
$$

Step 2. Divide by $10$ and identify the time constant.

$$
\frac{dq}{dt}+500q=10 , \qquad RC=10\times2\times10^{-4}=2\times10^{-3} \text{ s}
$$

Step 3. Write the charge and the current, using $i=\frac{dq}{dt}$ and $q(0)=0$.

$$
q=0.02\left(1-e^{-500t}\right)
$$

$$
i=10e^{-500t}
$$

Step 4. Evaluate at $t=0.002$. The exponent is $1$.

$$
q=0.02\left(1-0.36788\right)=0.01264
$$

$$
i=10\times0.36788=3.68
$$

Step 5. Check. Substituting gives $10\times0.02\times500e^{-500t}+5000\times0.02\left(1-e^{-500t}\right)=100e^{-500t}+100-100e^{-500t}=100$, and the initial charge is zero. The initial current equals the battery voltage divided by the resistance, which is what the loop reduces to when the capacitor is empty.

Step 6. Interpret. The capacitor reaches $63$ per cent of its final charge after one time constant, $2$ milliseconds, and the current has by then fallen to $37$ per cent of its initial value.

### 4.13 Problem: a critically damped circuit

A circuit has an inductance of $0.5$ henries, a resistance of $4$ ohms and a capacitance of one eighth of a farad. The capacitor carries $0.01$ coulombs and the current is zero when the switch is closed with no battery in the loop. Classify the circuit, find the charge and the current, and find the largest current.

### 4.14 Solution: equal roots, so the linear factor appears

Step 1. Write the homogeneous equation.

$$
0.5\frac{d^{2}q}{dt^{2}}+4\frac{dq}{dt}+8q=0
$$

Step 2. Divide by $0.5$ and write the characteristic equation.

$$
q''+8q'+16q=0 , \qquad r^{2}+8r+16=0
$$

Step 3. Factor the characteristic polynomial and read the roots.

$$
\left(r+4\right)^{2}=0 , \qquad r=-4
$$

Step 4. Confirm the classification from the damping ratio and the critical resistance.

$$
\omega_{n}=\frac{1}{\sqrt{LC}}=\frac{1}{\sqrt{0.0625}}=4 , \qquad \zeta=\frac{R}{2}\sqrt{\frac{C}{L}}=\frac{4}{2}\sqrt{0.25}=1
$$

The circuit is critically damped, and the repeated root is $-\zeta\omega_{n}=-4$, as it must be.

Step 5. Write the general solution in the repeated-root form.

$$
q=\left(A+Bt\right)e^{-4t}
$$

Step 6. Impose the initial charge.

$$
q(0)=A=0.01
$$

Step 7. Differentiate and impose the zero initial current.

$$
i=q'=Be^{-4t}-4\left(A+Bt\right)e^{-4t} , \qquad i(0)=B-4A=0
$$

So $B=0.04$ and the charge is

$$
q=\left(0.01+0.04t\right)e^{-4t} .
$$

Step 8. Write the current.

$$
i=\left(0.04-0.04-0.16t\right)e^{-4t}=-0.16te^{-4t}
$$

Step 9. Find the largest current. The magnitude $0.16te^{-4t}$ is largest where its derivative vanishes, that is at $t=0.25$ seconds.

$$
\left|i\right|_{\max}=0.16\times0.25\times e^{-1}=0.0147
$$

Step 10. Check. Substituting $q$ and its derivatives into $q''+8q'+16q$ gives $\left(-0.16+0.64t\right)e^{-4t}+8\left(-0.16t\right)e^{-4t}+16\left(0.01+0.04t\right)e^{-4t}$, whose coefficients of $e^{-4t}$ are $-0.16+0.16$ and $0.64-1.28+0.64$, both zero. The initial charge is $0.01$ and the initial current is zero.

Step 11. Interpret. The charge falls from $0.01$ coulombs to zero without ever becoming negative, and the current is negative throughout, which means the capacitor discharges in the direction opposite to the one assumed positive. Critical damping is the fastest possible return without a reversal.

### 4.15 Problem: an underdamped circuit

A circuit has an inductance of $1$ henry, a resistance of $2$ ohms and a capacitance of one fifth of a farad. The capacitor carries $0.01$ coulombs and the current is zero at the instant of closing, with no battery in the loop. Find the charge and the current, the damping ratio, and the first instant at which the charge is zero.

### 4.16 Solution: complex roots give a decaying oscillation

Step 1. Write the equation and its characteristic equation.

$$
q''+2q'+5q=0 , \qquad r^{2}+2r+5=0
$$

Step 2. Solve for the roots by completing the square.

$$
\left(r+1\right)^{2}+4=0 , \qquad r=-1\pm2i
$$

Step 3. Write the general solution with the decay rate $1$ and the damped frequency $2$.

$$
q=e^{-t}\left(A\cos 2t+B\sin 2t\right)
$$

Step 4. Confirm the classification.

$$
\omega_{n}=\sqrt{5} , \qquad \zeta=\frac{2}{2}\sqrt{\frac{0.2}{1}}=0.4472 , \qquad \omega_{d}=2=\omega_{n}\sqrt{1-\zeta^{2}}
$$

Step 5. Impose the initial charge, then the zero initial current.

$$
q(0)=A=0.01
$$

$$
i=e^{-t}\left(\left(-A+2B\right)\cos 2t+\left(-B-2A\right)\sin 2t\right) , \qquad i(0)=-A+2B=0
$$

So $B=0.005$.

Step 6. State the charge and the current.

$$
q=e^{-t}\left(0.01\cos 2t+0.005\sin 2t\right)
$$

$$
i=-0.025e^{-t}\sin 2t
$$

Step 7. Combine the charge into a single cosine with a phase.

$$
q=0.01118e^{-t}\cos\left(2t-0.4636\right)
$$

Step 8. Find the first zero of the charge. Setting the bracket to zero gives $\tan 2t=-2$, so $2t=\pi-1.1071=2.0344$ and $t=1.017$ seconds.

Step 9. Check. Differentiating twice and substituting confirms the equation because the roots were used to build the solution; the initial charge is $0.01$ and the initial current is zero. The charge crosses zero once every half period of length $\pi$ seconds, each crossing smaller than the last, and the oscillation dies away with time constant $1$ second.

### 4.17 Problem: two masses on springs, released from a displaced position

Two masses of one kilogram each are joined as in Section 1.7 with stiffnesses $k_{1}=3$ and $k_{2}=2$ newtons per metre. The first mass is displaced $1$ metre to the left of its equilibrium position, the second $2$ metres to the right, and both are released from rest. Find both displacements at time $t$.

### 4.18 Solution: eigen-decompose, then fit four conditions

Step 1. Write the system in the standard form of Section 1.7 with the numerical values inserted.

$$
x_{1}''+5x_{1}-2x_{2}=0
$$

$$
x_{2}''-2x_{1}+2x_{2}=0
$$

Step 2. Write the matrix of the system.

$$
A=\begin{pmatrix} -5 & 2 \\ 2 & -2 \end{pmatrix}
$$

Step 3. Compute the characteristic polynomial and check it against trace and determinant.

$$
\det\left(A-\lambda I\right)=\left(-5-\lambda\right)\left(-2-\lambda\right)-4=\lambda^{2}+7\lambda+6
$$

The trace is $-7$ and the determinant is $10-4=6$, both matching the polynomial.

Step 4. Factor and read the eigenvalues.

$$
\lambda^{2}+7\lambda+6=\left(\lambda+1\right)\left(\lambda+6\right) , \qquad \lambda=-1 , \quad \lambda=-6
$$

The natural frequencies are therefore $1$ and $\sqrt{6}$ radians per second.

Step 5. Find an eigenvector for each eigenvalue. For $\lambda=-1$ the first row gives $-4v_{1}+2v_{2}=0$, so $v_{2}=2v_{1}$ and $v_{1}=\left(1,2\right)$. For $\lambda=-6$ the first row gives $v_{1}+2v_{2}=0$, so $v_{1}=\left(2,-1\right)$.

Step 6. Write the general solution with both modes and both phases.

$$
x_{1}=a_{1}\cos t+2a_{2}\cos\left(\sqrt{6}\,t\right)
$$

$$
x_{2}=2a_{1}\cos t-a_{2}\cos\left(\sqrt{6}\,t\right)
$$

The sine terms are omitted at once because the initial velocities are zero, and omitting them is equivalent to imposing two of the four conditions.

Step 7. Impose the initial displacements $x_{1}(0)=-1$ and $x_{2}(0)=2$.

$$
a_{1}+2a_{2}=-1 , \qquad 2a_{1}-a_{2}=2
$$

Step 8. Solve the pair. The second equation gives $a_{2}=2a_{1}-2$, and substitution into the first gives $5a_{1}=3$.

$$
a_{1}=\frac{3}{5} , \qquad a_{2}=-\frac{4}{5}
$$

Step 9. State the particular solution.

$$
x_{1}=\frac{3}{5}\cos t-\frac{8}{5}\cos\left(\sqrt{6}\,t\right)
$$

$$
x_{2}=\frac{6}{5}\cos t+\frac{4}{5}\cos\left(\sqrt{6}\,t\right)
$$

Step 10. Verify the first equation. Differentiating $x_{1}$ twice gives $-\frac{3}{5}\cos t+\frac{48}{5}\cos\left(\sqrt{6}\,t\right)$, and $5x_{1}-2x_{2}$ equals $3\cos t-8\cos\left(\sqrt{6}\,t\right)-\frac{12}{5}\cos t-\frac{8}{5}\cos\left(\sqrt{6}\,t\right)$, which is $\frac{3}{5}\cos t-\frac{48}{5}\cos\left(\sqrt{6}\,t\right)$, exactly the negative of the second derivative.

Step 11. Verify the second equation and the conditions. Differentiating $x_{2}$ twice gives $-\frac{6}{5}\cos t-\frac{24}{5}\cos\left(\sqrt{6}\,t\right)$, whose negative is $\frac{6}{5}\cos t+\frac{24}{5}\cos\left(\sqrt{6}\,t\right)$; and $2x_{1}-2x_{2}$ equals $\frac{6}{5}\cos t-\frac{16}{5}\cos\left(\sqrt{6}\,t\right)-\frac{12}{5}\cos t-\frac{8}{5}\cos\left(\sqrt{6}\,t\right)$, which is $-\frac{6}{5}\cos t-\frac{24}{5}\cos\left(\sqrt{6}\,t\right)$, as required. At $t=0$ the answers give $-1$ and $2$, and both velocities vanish.

### 4.19 Problem: an asymmetric pair of masses

Two masses of $1$ kilogram and $2$ kilograms are joined by springs of stiffness $2$ newtons per metre each, the first spring joining the lighter mass to a fixed point and the second joining the two masses. Find the matrix of the system and its normal frequencies.

### 4.20 Solution: eigenvalues of the mass-normalised matrix

Step 1. Insert $m_{1}=1$, $m_{2}=2$, $k_{1}=k_{2}=2$ into the matrix of Section 3.7.

$$
A=\begin{pmatrix} -3 & 2 \\ 1 & -1 \end{pmatrix}
$$

Step 2. Write the characteristic polynomial and check the trace and determinant.

$$
\lambda^{2}+4\lambda+1=0 , \qquad \text{trace}=-4 , \quad \det\left(A\right)=3-2=1
$$

Step 3. Solve by the quadratic formula.

$$
\lambda=\frac{-4\pm\sqrt{16-4}}{2}=-2\pm\sqrt{3}
$$

Both roots are negative, so both motions are oscillations with frequencies

$$
\omega_{1}=\sqrt{2-\sqrt{3}}=0.5176 , \qquad \omega_{2}=\sqrt{2+\sqrt{3}}=1.9319 .
$$

Step 4. Find the eigenvectors. For $\lambda=-2+\sqrt{3}$ the first row gives $\left(-1-\sqrt{3}\right)v_{1}+2v_{2}=0$, so $v_{2}=\frac{1+\sqrt{3}}{2}v_{1}$. For $\lambda=-2-\sqrt{3}$ the first row gives $\left(-1+\sqrt{3}\right)v_{1}+2v_{2}=0$, so $v_{2}=\frac{1-\sqrt{3}}{2}v_{1}$, which is negative and corresponds to the two masses moving in opposition.

Step 5. Check the identities. The product of the roots is $4-3=1$, which equals the determinant, and the sum is $-4$, which equals the trace, so the eigenvalues are correct.

Step 6. Interpret. The slower mode is the in-phase mode, in which the heavier mass moves about $1.37$ times as far as the lighter one in the same direction; the faster mode is the out-of-phase mode, in which the heavier mass moves in the opposite direction. Every motion of the pair is a sum of these two.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Where each law ceases to be valid

The exponential law is a statement about a rate that is proportional to the amount, and it fails as soon as any resource becomes scarce. A population in a closed habitat cannot double indefinitely, because the food supply does not double. The standard repair introduces a negative term proportional to the square of the population, giving the logistic equation

$$
\frac{dx}{dt}=kx-\lambda x^{2} ,
$$

where $\lambda>0$ is small when the habitat is large. Separating the variables and using partial fractions produces

$$
x(t)=\frac{x_{0}k}{\left(k-\lambda x_{0}\right)e^{-kt}+\lambda x_{0}} ,
$$

which satisfies the initial condition at $t=0$, tends to the carrying capacity $\frac{k}{\lambda}$ as $t\to\infty$, and reduces to the exponential when $\lambda$ is neglected. The lesson for this topic is that the pure exponential is the small-time approximation of a more complicated reality, and quoting a doubling time is only meaningful while the population is far below its limit.

Newton's law of cooling fails when the body is not well mixed, when it loses heat mainly by evaporation or radiation rather than by convection, or when the excess is so large that the mechanism changes. In those cases the constant $k$ is not constant, and the exponential is only a rough fit over a limited range.

The tank model fails when the tank is not well stirred, when the outflow is drawn preferentially from the top or the bottom, when the solute reacts, or when the tank overflows. The first three destroy the identification of the outgoing concentration with $Q/V$; the fourth changes the volume balance. A reacting solute adds a sink term to the right-hand side that is usually non-linear in $Q$.

The circuit models assume constant $R$, $L$ and $C$. A real coil has resistance that grows with temperature, a real capacitor leaks, and a real battery's voltage falls as it supplies current. If the applied voltage is sinusoidal the model remains linear and solvable, but the arithmetic is heavier.

The spring model assumes Hooke's law and the absence of friction. Beyond the elastic limit the restoring force grows faster than the displacement, and the equations become non-linear; with friction the equations acquire a term proportional to velocity, and the two normal modes decay.

### 5.2 Forced oscillation and resonance

For a circuit with all three elements driven by a sinusoidal supply, the steady charge is again sinusoidal with the same frequency but a different phase, and its amplitude is

$$
Q_{0}=\frac{E_{0}}{\sqrt{\left(\frac{1}{C}-\omega^{2}L\right)^{2}+\omega^{2}R^{2}}} .
$$

The amplitude is largest when the bracket in the first term vanishes, that is when $\omega=\frac{1}{\sqrt{LC}}$, which is the natural frequency. At that frequency the amplitude is $\frac{E_{0}}{\omega R}$ and the current amplitude is $\frac{E_{0}}{R}$, which is the value the resistance alone would allow. This is resonance: a small resistance produces a large response, and the phase lag passes through a quarter of a cycle exactly at the natural frequency.

Resonance is the reason the classification of Section 2.5 matters in practice. A lightly damped circuit, with $\zeta$ well below one, has a sharp resonance and rings for many cycles after a disturbance; a heavily damped circuit has a broad, low resonance and settles at once.

### 5.3 Extensions of the spring system

The two-mass system generalises in three directions worth knowing. Adding a third mass produces a third-order matrix problem with three normal frequencies, and the same eigenvalue method applies without change. Adding damping proportional to the relative velocity of the masses adds a term proportional to $x'$ and makes the modes decay. Adding an external periodic force produces a forced system whose response is largest when the forcing frequency is near one of the normal frequencies, which is the mechanical analogue of resonance.

There is also a limiting case that links the topic to single-oscillator problems. If the first spring is very stiff, the first mass barely moves and the second mass behaves like a single mass on a single spring, with frequency $\sqrt{\frac{k_{2}}{m_{2}}}$. The two-mode solution reduces to that single frequency because the amplitude of the second mode is negligible.

### 5.4 Common errors

- **Using the inflow concentration in the outflow term.** The outgoing liquid carries the tank's concentration $Q/V$. Writing $c_{in}$ there makes the right-hand side independent of $Q$, so the model predicts a linear growth of salt that never saturates, contradicts the physics, and fails the check that the tank should approach the strength of its feed.
- **Forgetting to update the volume.** When the entry and exit rates differ, the volume is $V_{0}+\left(r_{in}-r_{out}\right)t$ and must appear in the coefficient of $Q$. Using the initial volume throughout is correct only for the first instant.
- **Dropping the initial condition or applying it too early.** The constant must be fixed after the general solution is complete. Fixing it before the particular integral has been added produces a solution that satisfies the condition but not the equation.
- **Confusing charge with current.** The charge is the state variable of the second-order circuit and the current is its derivative. A question that asks for the current requires one more differentiation, and a question that gives the initial current requires the derivative of the charge to be set correctly.
- **Mixing the signs of the cooling law.** The excess is the body's temperature minus the surroundings. Reversing the order of subtraction turns cooling into warming, and with a negative $k$ the model becomes unstable.
- **Misreading the damping classification.** The sign of $R^{2}-\frac{4L}{C}$, not the size of $R$ alone, decides the case. A circuit with a large inductance can be underdamped even with a substantial resistance, and a circuit with a small inductance can be overdamped with a modest one.
- **Using the wrong repeated-root form.** At critical damping the solution is $\left(A+Bt\right)e^{-rt}$, not $Ae^{rt}+Be^{rt}$. The second form cannot satisfy two independent initial conditions with distinct values.
- **Treating an eigenvalue as a frequency.** The eigenvalue of the matrix is $-\omega^{2}$. The frequency is the square root of its negative, and forgetting the sign produces imaginary frequencies from a system that oscillates perfectly well.
- **Losing the four conditions in a two-mass problem.** Two second-order equations carry four constants, and the initial velocities as well as the initial displacements are needed.
- **Assuming that the steady state is reached exactly.** Every exponential transient decays without ever vanishing, so statements about the long run must be phrased as limits or as approximations within a stated tolerance.

### 5.5 A summary of the five models

The five models of this topic differ in their physics and agree in their mathematics. Each is a linear equation or system with constant coefficients, each has a solution built from exponentials and sinusoids, and each is solved by identifying a steady state and a transient.

The growth and decay model is $\frac{dx}{dt}=kx$ with $x=x_{0}e^{kt}$, and its characteristic number is the doubling time or half-life $\frac{\ln 2}{|k|}$.

The cooling model is $\frac{dT}{dt}=-k\left(T-T_{s}\right)$ with $T=T_{s}+\left(T_{0}-T_{s}\right)e^{-kt}$, and its characteristic number is the cooling constant $k$, equivalently the time in which the excess halves.

The mixture model is $\frac{dQ}{dt}=c_{in}r_{in}-\frac{Q}{V}r_{out}$ with $V=V_{0}+\left(r_{in}-r_{out}\right)t$ and solution $Q=c_{in}V+CV^{-r_{out}/\left(r_{in}-r_{out}\right)}$, and its characteristic number is the steady mass $c_{in}V$.

The first-order circuit is $L\frac{di}{dt}+Ri=E$ with $i=\frac{E}{R}+\left(i_{0}-\frac{E}{R}\right)e^{-Rt/L}$, and its characteristic number is the time constant $\frac{L}{R}$.

The second-order circuit is $Lq''+Rq'+q/C=E$ with behaviour fixed by $\Delta=R^{2}-\frac{4L}{C}$ and steady charge $CE$, and its characteristic numbers are the natural frequency $\omega_{n}$, the damping ratio $\zeta$ and, in the underdamped case, the damped frequency $\omega_{d}$.

The spring system is $Mx''=Kx$ with solution a sum of normal modes, and its characteristic numbers are the eigenvalues of $M^{-1}K$.

Anyone who can state these six sentences, derive each from its law, and verify each against its initial condition has the whole topic at command.
