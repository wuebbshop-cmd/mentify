## 1. Foundational Concepts, Definitions, and Axioms

### 1.1 Picture a kettle cooling on a windowsill

Imagine a kettle of very hot water standing on a windowsill in a cool kitchen. Nobody lifts it, nobody stirs it, the window stays shut. The water cools. What is worth noticing is not that it cools but the way it cools: during the first five minutes the thermometer falls a long way, during the next five minutes it falls less, and after half an hour the fall is barely visible. The water is chasing the temperature of the room and never quite arrives at it.

Picture a second scene: a small tank of salty water. One pipe drips brine into the tank, a stirrer keeps the tank uniform, and a second pipe lets the mixture run out. The amount of salt inside rises quickly at first, then more and more slowly, and finally levels off. Picture a third scene: a battery, a coil of wire and a lamp joined into one loop, with a switch that is closed at a chosen instant. The lamp is dim at the moment of closing and brightens over the following fraction of a second. Picture a fourth scene: two laboratory trolleys joined to each other and to a wall by springs on a smooth bench. Pull one trolley aside and release it, and both trolleys begin to move, each at its own rhythm, in a pattern that looks complicated but repeats.

The four scenes have exactly the same structure. In each there is a quantity that changes: a temperature, a mass of salt, a current, a displacement. In each there is a statement of how fast that quantity changes, and the statement mentions the quantity itself. In each there is a starting fact: the temperature when you began to watch, the salt present at the start, the current at the instant of closing the switch, the displacement at the moment of release. The statement about speed is a differential equation, the starting fact is called a condition, and the pair together determine the quantity at every later moment.

That is the whole business of this topic. You read a physical sentence, you translate it into an equation about a rate of change, you solve the equation, and then you read the answer back into the language of the physical situation.

### 1.2 The two letters that carry the subject

In every one of the scenes above there is one quantity that changes and one clock that drives the change. Give them letters.

The clock is $t$, and it stands for time, measured in whatever unit the problem uses: minutes for the kettle, minutes for the tank, seconds for the circuit, seconds for the trolleys. It is called the independent variable, because you are free to choose which moment to examine.

The changing quantity is called the dependent variable, because its value depends on which moment you choose. For the kettle it is the temperature and we write $T$, measured in degrees Celsius. For the tank it is the mass of dissolved salt and we write $Q$, measured in kilograms. For the circuit it is the current and we write $i$, measured in amperes. For the first trolley it is a displacement and we write $x_1$, measured in metres.

The symbol $\frac{dT}{dt}$ means the rate at which $T$ changes as $t$ changes. If $T$ is measured in degrees and $t$ in minutes, then $\frac{dT}{dt}$ is measured in degrees per minute. It is a single symbol, not a fraction to be pulled apart, and it answers one question: at this instant, how fast is the quantity changing? A steep fall means a large negative value, a gentle fall means a small negative value, and no change at all means the value is zero.

Every symbol in what follows will be named in words when it first appears, and the units will be named too. Units matter here more than in most of mathematics, because a differential equation coming from a physical story is only meaningful when both sides carry the same units. The left side of $\frac{dQ}{dt}=0.2-0.02Q$ is a rate in kilograms per minute; the number $0.2$ must therefore also be a rate in kilograms per minute, and the product $0.02Q$ must be too.

The table below lists the applications treated in this note, with the quantity that changes and the physical law that supplies the rule.

| Application | Quantity that changes | Physical law that gives the rule |
| --- | --- | --- |
| Growth and decay | a population or an amount | rate of change proportional to the amount present |
| Cooling | a temperature | rate of cooling proportional to the excess over the room |
| Mixture | mass of salt in a tank | what enters minus what leaves |
| First-order circuit | current or charge | Kirchhoff's voltage law |
| Second-order circuit | charge on a capacitor | Kirchhoff's voltage law with three components |
| Two springs | two displacements | Hooke's law with Newton's second law |

### 1.3 Growth: when the rate is proportional to the amount

Think of a colony of bacteria in a dish. Each bacterium divides after a fixed time, so the number of new bacteria produced in a minute is proportional to the number already there. Twice as many bacteria produce twice as many new ones. Put into symbols: let $x$ be the number of bacteria at time $t$, measured in minutes, and let $k$ be a positive constant called the per-head growth rate, measured per minute. The rule is then

$$
\frac{dx}{dt}=kx .
$$

The constant $k$ carries the meaning of "new bacteria per minute for each bacterium present". If there are $100$ bacteria and they produce $5$ new ones per minute, then $5=k\cdot 100$, so $k=0.05$ per minute. That single number, together with the starting count, fixes the whole future of the colony.

The solution of the rule is an exponential:

$$
x=100e^{0.05t},
$$

where the number $e$ is a fixed constant equal to about $2.718$. The number $e$ is not chosen by us; it is the number that appears whenever a quantity grows at a rate proportional to itself, in the same way that $\pi$ appears whenever a circle is measured.

Check the answer against the rule. The derivative of $100e^{0.05t}$ is $0.05$ multiplied by $100e^{0.05t}$, that is $0.05x$, which is exactly what the rule demands. Check the starting fact: at $t=0$ the exponential is $1$, so $x=100$, as required.

Small numbers make the meaning visible. At $t=20$ minutes the factor is $e^{1}=2.718$, so the colony has grown to about $272$ bacteria. The time needed to double is the same whatever the starting count, and it is about $13.9$ minutes here, because doubling requires a factor of $2$ and the factor $2$ is reached when $0.05t=\ln 2$. The symbol $\ln$ means the natural logarithm, the inverse of the exponential.

### 1.4 Decay: the same rule with a minus sign

Radioactive material behaves like the bacteria in reverse. The number of nuclei that disintegrate in a minute is proportional to the number still present, but the change is a loss, so the rule carries a minus sign. If $x$ is the mass of the substance in grams and $t$ is time in days, the rule is

$$
\frac{dx}{dt}=-kx ,
$$

with $k$ a positive number. Take $100$ grams of a substance whose half-life is $10$ days, meaning that after $10$ days only $50$ grams remain. The solution is

$$
x=100\left(\frac{1}{2}\right)^{t/10},
$$

and after $30$ days the factor is one eighth, so $12.5$ grams remain. The same answer is written with the exponential as $x=100e^{-0.0693t}$, because the constant $k$ equals $\ln 2$ divided by the half-life, that is $0.693$ divided by $10$.

The two rules differ only in the sign of the constant, and that is the first habit to acquire: a plus sign describes growth, a minus sign describes decay, and the constant is positive in both cases. Writing $k$ itself as negative and then adding a second minus sign is the commonest source of confusion in this whole topic.

### 1.5 Cooling: the rate depends on the gap

A cooling body does not obey the growth rule. Its rate of cooling depends not on its temperature but on how far its temperature is above the temperature of the room. This is Newton's law of cooling, stated in words: the rate at which a body loses heat is proportional to the difference between its own temperature and the temperature of its surroundings.

Let $T$ be the temperature of the water in degrees Celsius at time $t$ in minutes, and let $T_s$ be the fixed temperature of the room. The word "difference" gives the rule

$$
\frac{dT}{dt}=-k\left(T-T_s\right),
$$

where $k$ is a positive constant measured per minute, and the minus sign records that a body warmer than the room cools rather than warms. The bracket is the excess of the water over the room, in degrees.

Suppose the room is at $20$ degrees, the water starts at $90$ degrees, and at the first instant the water is losing $2$ degrees per minute. Then the excess is $70$ degrees and the rate is $-2$, so $2=k\cdot 70$ and $k=0.0286$ per minute. The solution is

$$
T=20+70e^{-0.0286t}.
$$

Check the starting fact: at $t=0$ the exponential is $1$ and $T=90$. Check the rule: the derivative is $-70(0.0286)e^{-0.0286t}$, which equals $-2$ when $t=0$ and becomes smaller in size as time passes. Check the long run: as $t$ becomes large the exponential shrinks to nothing and $T$ approaches $20$, the room temperature. After $24$ minutes, for instance, the exponential is $0.503$ and the water is at about $55$ degrees.

The structure of the answer is worth memorising in words: the temperature equals the room temperature plus the initial excess multiplied by a decaying exponential. Every cooling question in the course is this sentence with different numbers.

### 1.6 The salt tank: what enters minus what leaves

Imagine a tank holding $100$ litres of water in which $5$ kilograms of salt are dissolved. Brine containing $0.1$ kilograms of salt per litre flows in at $2$ litres per minute, the contents are kept uniform by stirring, and the mixture flows out at the same $2$ litres per minute. Because the same volume enters and leaves, the tank always holds $100$ litres.

The bookkeeping sentence is short: the rate at which the salt in the tank changes equals the rate at which salt enters minus the rate at which salt leaves. Let $Q$ be the mass of salt in the tank in kilograms at time $t$ in minutes.

Salt enters at $2$ litres per minute, and each litre carries $0.1$ kilograms, so the entry rate is $2\times 0.1=0.2$ kilograms per minute.

Salt leaves at $2$ litres per minute, but the leaving liquid is not brine of strength $0.1$; it is the well-stirred contents of the tank. The concentration inside the tank is the mass divided by the volume, that is $Q/100$ kilograms per litre. So the exit rate is $2\times\left(Q/100\right)=0.02Q$ kilograms per minute.

The rule is therefore

$$
\frac{dQ}{dt}=0.2-0.02Q ,
$$

and the starting fact is that $Q=5$ when $t=0$. The solution is

$$
Q=10-5e^{-0.02t}.
$$

Check the starting fact: at $t=0$ the exponential is $1$ and $Q=5$. Check the rule: the derivative is $0.1e^{-0.02t}$, while the right-hand side is $0.2-0.02\left(10-5e^{-0.02t}\right)=0.1e^{-0.02t}$. Check the long run: the exponential dies away and $Q$ tends to $10$ kilograms, which is exactly the mass the tank would hold if it were filled with the incoming brine, since $100$ litres at $0.1$ kilograms per litre is $10$ kilograms.

That final value is called the steady state, and the word steady means that the entering and leaving rates have become equal so that the amount stops changing. Notice how the answer behaves: the amount rises quickly while the tank is much fresher than the inflow, and then more slowly as the two strengths approach each other.

The one trap in this section is worth stating immediately, because it spoils more mixture solutions than any other mistake. The concentration used in the exit rate is the concentration of the tank, not the concentration of the inflow. Multiplying the outflow rate by $0.1$ would give a constant exit rate of $0.2$ kilograms per minute, which would make the right-hand side zero and would say that the salt never changes, an absurd conclusion.

### 1.7 Circuits: voltage shared among components

An electrical circuit in series has four possible kinds of component, and each has a name, a symbol and a unit. The electromotive force, written $E$ and measured in volts, is the driving source, usually a battery. The resistance, written $R$ and measured in ohms, is the component that opposes the flow of current. The inductance, written $L$ and measured in henries, is a coil that opposes changes in current. The capacitance, written $C$ and measured in farads, is a component that stores charge.

Two further quantities describe what happens. The current, written $i$ and measured in amperes, is the rate at which charge flows through the wire. The charge, written $q$ and measured in coulombs, is the amount of electricity that has accumulated on the capacitor. They are related by the sentence "current is the rate at which charge arrives":

$$
i=\frac{dq}{dt}.
$$

Kirchhoff's voltage law says in words that the voltage supplied by the source is shared among the components in the loop, so the sum of the voltage drops across the components equals the supply. The inductor's drop is $L\frac{di}{dt}$, the resistor's drop is $Ri$, and the capacitor's drop is $q$ divided by $C$. A circuit with a battery, a resistor and an inductor therefore satisfies

$$
L\frac{di}{dt}+Ri=E ,
$$

and a circuit with all three kinds of component satisfies

$$
L\frac{d^{2}q}{dt^{2}}+R\frac{dq}{dt}+\frac{q}{C}=E .
$$

The second equation is obtained from the first by replacing the current with the rate of change of charge and noting that the derivative of the current is then the second derivative of the charge.

A first set of small numbers makes the first equation concrete. Take a battery of $12$ volts, a resistance of $2$ ohms and an inductance of $1$ henry, and close the switch when no current is flowing. The equation is

$$
\frac{di}{dt}+2i=12 .
$$

Its solution is

$$
i=6\left(1-e^{-2t}\right),
$$

with $t$ in seconds and $i$ in amperes. Check the starting fact: at $t=0$ the bracket is zero and so is the current. Check the rule: the derivative is $12e^{-2t}$, and the left-hand side is $12e^{-2t}+12\left(1-e^{-2t}\right)=12$, the supply. Check the long run: the exponential dies and the current settles at $6$ amperes, which is the supply divided by the resistance.

A second set of numbers shows the capacitor. Take a battery of $10$ volts, a resistance of $2$ ohms and a capacitance of one quarter of a farad, and start with an uncharged capacitor. The capacitor's drop is $q$ divided by $C$, which is $4q$, so the equation is

$$
2\frac{dq}{dt}+4q=10 ,
$$

whose solution with $q=0$ at the start is

$$
q=2.5\left(1-e^{-2t}\right),
$$

in coulombs. The current is the derivative, $i=5e^{-2t}$ amperes: it starts at its largest value, the supply divided by the resistance, and fades as the capacitor fills. The charge and the current are therefore different answers to different questions, and a solution that confuses them is wrong even when the arithmetic is right.

A third set of numbers shows the second-order case with no resistance at all. Take an inductance of $1$ henry, a capacitance of one quarter of a farad, no resistance, and no battery, and start with one coulomb of charge and no current. The equation is

$$
\frac{d^{2}q}{dt^{2}}+4q=0 ,
$$

whose solution is $q=\cos 2t$ coulombs. The charge swings back and forth forever between one coulomb and minus one coulomb, and the current is $-2\sin 2t$ amperes. Adding resistance to such a circuit makes the swing die away instead of lasting, and the amount of resistance decides whether the charge crosses zero, just touches it, or slides back without crossing at all.

### 1.8 Two trolleys joined by springs

Place a smooth horizontal bench. Fix a point $P$ at one end. Attach a spring of stiffness $k_1$ to $P$, attach a trolley of mass $m_1$ to the other end of that spring, attach a second spring of stiffness $k_2$ to the trolley, and attach a second trolley of mass $m_2$ to the far end of the second spring. Stiffness is measured in newtons per metre and means the force the spring exerts per metre of stretch.

Let $x_1$ be the distance the first trolley has been displaced to the right of its resting position, in metres, and let $x_2$ be the corresponding displacement of the second trolley. Both are functions of the time $t$ in seconds.

Two laws supply the rules. Hooke's law says in words that a spring pulls back with a force proportional to the distance it has been stretched. Newton's second law says in words that mass times acceleration equals the total force.

The first spring is stretched by $x_1$, so it pulls the first trolley back with force $k_1x_1$ to the left. The second spring is stretched by the difference $x_2-x_1$, so it pushes the first trolley to the right with force $k_2\left(x_2-x_1\right)$, and it pulls the second trolley to the left with the same force. With masses of one kilogram each, stiffnesses of $3$ and $2$ newtons per metre, the two rules become

$$
\frac{d^{2}x_1}{dt^{2}}=-3x_1+2\left(x_2-x_1\right) ,
$$

$$
\frac{d^{2}x_2}{dt^{2}}=-2\left(x_2-x_1\right) .
$$

These are two equations in two unknown functions, and neither can be solved without the other: that is why the topic is called a system.

One motion is easy to guess. Suppose the first trolley is pulled $1$ metre to the right and the second is pulled $2$ metres, and both are released from rest. Then $x_1=\cos t$ and $x_2=2\cos t$ satisfies both equations, as substitution shows, and the two trolleys move in step, the second always twice as far as the first. This is the first natural rhythm of the pair.

A second motion is equally easy. Suppose the displacements are in the ratio two to minus one, that is $x_1=2\cos\left(\sqrt{6}\,t\right)$ and $x_2=-\cos\left(\sqrt{6}\,t\right)$, again released from rest. Substitution shows that this also satisfies both equations, and here the trolleys move in opposite directions with a faster rhythm.

Every motion of the pair is a mixture of these two rhythms, which are called the normal modes. Part of the work of this topic is to find the rhythms, and part is to work out how much of each rhythm a given starting position demands.

### 1.9 Conditions, and what it means to have solved the problem

A differential equation by itself describes a whole family of possible histories, one for each starting value. The equation $\frac{dx}{dt}=kx$ is satisfied by $x=100e^{kt}$ and by $x=7e^{kt}$ and by every other multiple. To pick out the history that actually happens you must supply a starting fact, called an initial condition, such as $x=100$ when $t=0$.

The number of starting facts needed equals the order of the equation, that is the order of the highest derivative present. A first-order equation such as the growth rule needs one condition, because its solution contains one constant to be fixed. A second-order equation such as the circuit with a capacitor needs two conditions, usually the charge and the current at the start, because its solution contains two constants.

To solve a problem of this kind means four things, and all four are expected in a complete answer. First, name the variables and their units. Second, state the physical law in words and translate it into an equation. Third, solve the equation and use the condition to fix the constant. Fourth, check the answer by substituting it back and by asking whether its long-run behaviour makes physical sense.

## 2. Theorems, Lemmas, and Analytical Properties

### 2.1 The growth and decay theorem

> **Theorem (Natural growth and decay).** Let $k$ be a constant. Every solution of the equation $\frac{dx}{dt}=kx$ has the form $x=x_0e^{kt}$, where $x_0$ is the value of $x$ at $t=0$. If $k$ is positive the quantity grows, if $k$ is negative it decays, and if $k$ is zero it stays constant.

The theorem does two jobs at once. It says that the only histories allowed by the rule are exponential ones, and it says that the single number $x_0$ together with the single number $k$ determines everything. No other shape of answer is possible, so a solution that is not exponential is simply wrong.

> **Corollary (Doubling time and half-life).** For natural growth with positive $k$, the quantity doubles in the time $\frac{\ln 2}{k}$, whatever its starting value. For natural decay with positive $k$ in the equation $\frac{dx}{dt}=-kx$, the quantity halves in the time $\frac{\ln 2}{k}$, whatever its starting value.

The corollary is the reason radiocarbon dating and bacterial growth estimates work. The doubling time does not depend on how much is present, so a sample of one gram and a sample of one tonne double in step. In the bacteria example the doubling time was $\ln 2$ divided by $0.05$, which is about $13.9$ minutes, and it would be $13.9$ minutes for a colony of any size.

The constant $k$ and the doubling time carry the same information, and each can be found from the other. If a population doubles in $50$ years, then $k$ equals $\ln 2$ divided by $50$, about $0.0139$ per year. If instead you are told that a population grows by $2$ per cent per year, then $k$ is close to $0.02$ per year, but not equal to it, because the two per cent is applied to a changing amount; the exact statement is $e^{k}=1.02$, so $k=\ln 1.02=0.0198$. That small difference is a favourite examination trap.

### 2.2 The cooling theorem

> **Theorem (Newton's law of cooling).** For a body in surroundings of constant temperature $T_s$, the solution of $\frac{dT}{dt}=-k\left(T-T_s\right)$ with initial temperature $T_0$ is $T=T_s+\left(T_0-T_s\right)e^{-kt}$.

Three properties follow and each is worth a sentence in an answer.

The first is that the excess over the room decays exponentially. If you write $u=T-T_s$ for the excess, the rule becomes $\frac{du}{dt}=-ku$, which is exactly the decay rule of Section 2.1. Recognising this reduction turns an unfamiliar problem into a familiar one.

The second is that the temperature approaches the room temperature from whichever side it starts on but never reaches it in finite time, because an exponential is never zero. Physically, an object at room temperature has no excess to lose, so it stops changing.

The third is that the body never overshoots. A cooling object cannot become colder than the room by this law, since the moment it reached room temperature the right-hand side would be zero and it would stay there.

### 2.3 The mixture theorems

> **Theorem (Mass balance for a well-stirred tank).** If brine of concentration $c_{in}$ enters at the volume rate $r_{in}$ and the well-stirred contents leave at the volume rate $r_{out}$, then the mass $Q$ of dissolved substance satisfies $\frac{dQ}{dt}=c_{in}r_{in}-\frac{Q}{V(t)}r_{out}$, where $V(t)=V_0+\left(r_{in}-r_{out}\right)t$ is the volume at time $t$.

This is the only rule needed for every tank problem in the course, and every symbol has a plain meaning: $c_{in}$ is kilograms per litre in the incoming pipe, $r_{in}$ and $r_{out}$ are litres per minute, $V$ is litres, and $Q$ is kilograms. The fraction $Q/V$ is the concentration inside the tank, and it is this fraction, not $c_{in}$, that multiplies the outflow rate.

> **Theorem (Steady state).** When the entering and leaving volume rates are equal, so that the volume is constant, and when $c_{in}$ is constant, the mass tends to $c_{in}V$ as time increases, and the concentration in the tank tends to $c_{in}$.

The theorem confirms common sense: a tank through which the same brine circulates forever ends up with the same strength as the brine being fed to it. In the example of Section 1.6 the limit was $0.1$ times $100$, that is $10$ kilograms, which matched the computed limit.

A useful further property concerns the direction of change. When the tank is fresher than the inflow, so that $Q$ is below $c_{in}V$, the entry rate exceeds the exit rate and $Q$ increases. When the tank is saltier than the inflow, $Q$ decreases. So the mass always moves toward the steady state and never away from it, which is a check you can apply to any solution you obtain.

### 2.4 The first-order circuit theorems

> **Theorem (Inductive circuit).** For constant $E$, $R$ and $L$, the solution of $L\frac{di}{dt}+Ri=E$ with $i=0$ at $t=0$ is $i=\frac{E}{R}\left(1-e^{-Rt/L}\right)$. The current tends to $\frac{E}{R}$ and the quantity $\frac{L}{R}$ is called the time constant.

The ratio $\frac{E}{R}$ is the current that Ohm's law alone would give, and the theorem says that the coil prevents the current from reaching it instantly. The time constant is measured in seconds, since henries divided by ohms is seconds, and it measures how quickly the coil's opposition fades.

> **Theorem (Capacitive circuit).** For constant $E$, $R$ and $C$, the solution of $R\frac{dq}{dt}+\frac{q}{C}=E$ with $q=0$ at $t=0$ is $q=CE\left(1-e^{-t/(RC)}\right)$, and the current is $i=\frac{E}{R}e^{-t/(RC)}$.

Here the time constant is $RC$, again in seconds, and the final charge is $CE$ coulombs. The current starts at $\frac{E}{R}$, the value it would have if the capacitor were a plain wire, and decays as the capacitor charges. The two theorems are the same theorem wearing different clothes: both are first-order linear equations with a constant right-hand side, and both solutions consist of a final value plus a decaying exponential.

### 2.5 The second-order circuit classification

> **Theorem (Classification of the RLC circuit).** For $L\frac{d^{2}q}{dt^{2}}+R\frac{dq}{dt}+\frac{q}{C}=0$ with $L$, $R$, $C$ positive, form the quantity $R^{2}-\frac{4L}{C}$. If it is negative the circuit is underdamped and the charge oscillates with a decaying amplitude. If it is zero the circuit is critically damped and the charge returns to zero without oscillating about it. If it is positive the circuit is overdamped and the charge returns to zero slowly, again without oscillating.

Each case corresponds to a different kind of answer. In the underdamped case the answer contains a cosine and a sine multiplied by a decaying exponential, so the charge swings above and below zero while shrinking. In the critically damped case the answer contains a linear term multiplied by a decaying exponential, which is the borderline between swinging and not swinging. In the overdamped case the answer is a sum of two decaying exponentials with different rates, so the charge creeps back without ever swinging.

In the special case of no resistance at all, the equation becomes $\frac{d^{2}q}{dt^{2}}+\frac{q}{LC}=0$, whose solutions are pure cosines and sines with angular frequency $\frac{1}{\sqrt{LC}}$. The charge then oscillates forever, and the circuit is a perfect pendulum.

### 2.6 The two-spring theorems

> **Theorem (Normal modes).** For two masses joined by springs as in Section 1.8, every motion is a sum of two special motions called normal modes, and in each normal mode both masses vibrate with the same frequency and with a fixed ratio of amplitudes.

For the numbers of Section 1.8 the two frequencies were $1$ radian per second and $\sqrt{6}$ radians per second, and the corresponding amplitude ratios were $1$ to $2$ and $2$ to $-1$. The first mode has the trolleys moving together, the second has them moving apart and together in opposition.

> **Lemma (Order of the system).** A system of two second-order equations requires four initial conditions, usually the two displacements and the two velocities at the starting instant.

The count is not a convention. Each second-order equation brings two constants when solved, so the pair brings four, and four conditions are needed to fix them. This is why the trolley problems always state where each trolley starts and that it starts from rest.

### 2.7 What every answer should look like

Five properties can be checked on any answer, and a solution that fails one of them is wrong.

The first is that it satisfies the differential equation identically. Substitute and simplify; the two sides must agree for all $t$ in the range.

The second is that it satisfies the condition. Put $t=0$ into the answer and confirm the stated starting value.

The third is that its units are right. A temperature answer must be a temperature, a current answer must be an ampere, and no formula that adds degrees to minutes can be correct.

The fourth is that its long-run behaviour is physically sensible. A cooling body tends to room temperature, an inductive circuit tends to the Ohm's law current, a tank tends to the strength of its inflow.

The fifth is that its short-run behaviour matches the starting rate. If the problem says the water is losing two degrees per minute at the start, the derivative of your answer at $t=0$ must be $-2$.

## 3. Formal Proofs, Derivations, and Methods

### 3.1 Method: solving a growth or decay rule

The rule $\frac{dx}{dt}=kx$ is solved by separating the two letters. The idea is to get everything containing $x$ on one side and everything containing $t$ on the other, and then to integrate.

Step 1. Divide both sides by $x$. This is allowed wherever $x$ is not zero, and in a growth or decay problem $x$ is a positive amount.

$$
\frac{1}{x}\frac{dx}{dt}=k
$$

Step 2. Integrate both sides with respect to $t$. On the left the chain rule turns the integral into an integral in $x$.

$$
\int\frac{1}{x}\,dx=\int k\,dt
$$

Step 3. Perform the integrations. One constant is enough, because only one integration in total has been performed.

$$
\ln x=kt+C
$$

Step 4. Undo the logarithm by exponentiating both sides, and write the constant $e^{C}$ as a new positive constant $A$.

$$
x=Ae^{kt}
$$

Step 5. Fix $A$ from the starting fact. If $x=x_0$ when $t=0$, then $x_0=Ae^{0}=A$, so the answer is $x=x_0e^{kt}$.

Step 6. Check. The derivative of $x_0e^{kt}$ is $kx_0e^{kt}$, which is $kx$, so the rule holds, and at $t=0$ the value is $x_0$, so the condition holds.

For decay the same six steps apply with $k$ replaced by $-k$, and the answer becomes $x=x_0e^{-kt}$. Nothing else changes.

### 3.2 Method: solving a cooling rule

Step 1. Write the excess as a single letter, $u=T-T_s$. This is not a trick for its own sake: it turns the problem into the one just solved.

Step 2. Differentiate the definition of $u$. Since $T_s$ is a constant, $\frac{du}{dt}=\frac{dT}{dt}$.

Step 3. Substitute into the cooling rule.

$$
\frac{du}{dt}=-ku
$$

Step 4. Use the result of Section 3.1 to write $u=u_0e^{-kt}$, where $u_0$ is the initial excess.

Step 5. Translate back into temperatures.

$$
T=T_s+\left(T_0-T_s\right)e^{-kt}
$$

Step 6. Fix $k$ from a second fact, such as a temperature observed at a later time. If $T$ equals some stated value at $t=t_1$, substitute both numbers and solve for $k$ using a logarithm.

Step 7. Check by substituting $t=0$ and by examining the limit as $t$ grows.

### 3.3 Method: solving a mixture problem

Step 1. Name the unknown: $Q$, the mass of dissolved substance in the tank, in kilograms, at time $t$.

Step 2. Compute the entry rate as the product of the inflow volume rate and the inflow concentration. Both factors must be in the units of the problem.

Step 3. Compute the exit rate as the product of the outflow volume rate and the concentration in the tank, which is $Q$ divided by the volume.

Step 4. Write the balance rule.

$$
\frac{dQ}{dt}=\left(\text{entry rate}\right)-\left(\text{exit rate}\right)
$$

Step 5. Write the volume as a function of time if the two rates differ. If they are equal the volume is constant and the equation has constant coefficients.

Step 6. Solve the resulting first-order linear equation, then impose the starting mass.

Step 7. Interpret the answer: state the long-run mass, the long-run concentration, and the time at which any stated fraction of the steady state is reached.

### 3.4 Method: solving an inductive circuit

Step 1. Write Kirchhoff's law for the loop, naming each component's drop.

Step 2. Substitute the numbers and divide through by the inductance so that the coefficient of the derivative is one.

Step 3. Multiply the whole equation by the integrating factor. For an equation $\frac{di}{dt}+pi=q$ with constant $p$, the integrating factor is $e^{pt}$, and the left side then collapses into a single derivative.

$$
\frac{d}{dt}\left(ie^{pt}\right)=qe^{pt}
$$

Step 4. Integrate both sides with respect to $t$, which introduces one constant.

Step 5. Divide by the integrating factor and impose the initial current.

Step 6. Check the initial current, the long-run current and the units.

For the numbers of Section 1.7 the coefficient is $p=2$ and the right side is $q=12$, so the integrating factor is $e^{2t}$ and the steps reproduce $i=6\left(1-e^{-2t}\right)$.

### 3.5 Method: solving a capacitive circuit

The same six steps apply, with the unknown being the charge rather than the current. The one extra care is to remember that the term $\frac{q}{C}$ is a voltage and not a current, so it must be divided by the resistance before it can be compared with the derivative term, or the whole equation must be divided by the resistance first.

For the numbers of Section 1.7, dividing $2\frac{dq}{dt}+4q=10$ through by $2$ gives $\frac{dq}{dt}+2q=5$, whose solution with $q=0$ at the start is $q=2.5\left(1-e^{-2t}\right)$.

### 3.6 Method: solving an undamped second-order circuit

Step 1. Write the equation in the form $\frac{d^{2}q}{dt^{2}}+\omega^{2}q=0$, where $\omega$ is the angular frequency in radians per second.

Step 2. Write the general solution as a combination of a cosine and a sine with the same frequency.

$$
q=A\cos\left(\omega t\right)+B\sin\left(\omega t\right)
$$

Step 3. Use the starting charge to fix $A$, since the cosine is one and the sine is zero at $t=0$.

Step 4. Differentiate to get the current, then use the starting current to fix $B$.

Step 5. Check both starting facts and confirm that the frequency is the one predicted by the coefficients.

### 3.7 Method: checking a two-spring solution

A proposed pair of displacements is checked one equation at a time.

Step 1. Differentiate each proposed displacement twice to obtain the two accelerations.

Step 2. Substitute into the first equation and collect the terms in each rhythm.

Step 3. Substitute into the second equation and collect again.

Step 4. Confirm that every collection vanishes. If one rhythm survives in either equation, the proposal is not a solution.

Step 5. Confirm that the starting conditions hold, and count the constants: two second-order equations need four conditions in total.

Step 6. If a full answer is required rather than a check, write a general combination of the two modes with four constants and solve the four conditions as simultaneous equations.

## 4. Representative Worked Examples and Solutions

### 4.1 Problem: a population with a known doubling time

A town has $5000$ inhabitants, and its population doubles every $20$ years. Assuming that the rate of increase is proportional to the population, find the rule, the population after $30$ years, and the year in which the population reaches $20\,000$.

### 4.2 Solution: convert the doubling time into the constant, then substitute

Step 1. Name the quantities. Let $x$ be the population after $t$ years, and let $k$ be the per-head growth rate in per year.

Step 2. Write the law in words and in symbols: the rate of increase is proportional to the population, so

$$
\frac{dx}{dt}=kx .
$$

Step 3. From the doubling time, find $k$. Doubling means that $x$ is twice its starting value when $t=20$, and the theorem of Section 2.1 says that the doubling time is $\frac{\ln 2}{k}$.

$$
k=\frac{\ln 2}{20}=0.03466
$$

Step 4. Write the solution with the starting population.

$$
x=5000e^{0.03466t}
$$

Step 5. Substitute $t=30$. The exponent is $1.0397$ and the exponential is $2.8284$, which is $2$ raised to the power one and a half, as it must be, since thirty years is one and a half doubling times.

$$
x=5000\times 2.8284=14\,142
$$

Step 6. Find the time to reach $20\,000$. Divide by $5000$ to get $4$, take logarithms, and divide by $k$.

$$
t=\frac{\ln 4}{0.03466}=\frac{1.3863}{0.03466}=40
$$

Step 7. Interpret and check. The answer is $14\,142$ people after $30$ years, and the population quadruples after $40$ years, which is two doublings and is therefore consistent. Substituting $t=0$ returns $5000$, and differentiating returns $kx$, so both the condition and the rule are satisfied.

### 4.3 Problem: a cooling cup

A cup of coffee at $80$ degrees Celsius stands in a room at $20$ degrees. After $5$ minutes it has cooled to $60$ degrees. Find the temperature after $15$ minutes and the temperature after a very long time.

### 4.4 Solution: form the excess, halve the work

Step 1. Name the quantities. Let $T$ be the temperature of the coffee in degrees at time $t$ in minutes, and let $T_s=20$ be the room temperature.

Step 2. Write Newton's law of cooling.

$$
\frac{dT}{dt}=-k\left(T-20\right)
$$

Step 3. Write the solution in the form of Section 2.2, with the initial excess $80-20=60$.

$$
T=20+60e^{-kt}
$$

Step 4. Use the observation at $t=5$ to find $k$. The excess there is $60-20=40$.

$$
40=60e^{-5k}
$$

$$
e^{-5k}=\frac{2}{3}
$$

$$
k=\frac{1}{5}\ln\frac{3}{2}=0.08109
$$

Step 5. Substitute $t=15$. Because fifteen minutes is three lots of five minutes, the exponential is the cube of two thirds.

$$
T=20+60\left(\frac{2}{3}\right)^{3}=20+60\times\frac{8}{27}=20+17.78=37.8
$$

Step 6. State the long-run temperature. As $t$ grows the exponential vanishes and $T$ approaches $20$ degrees, the room temperature.

Step 7. Check. At $t=0$ the answer gives $80$ degrees, at $t=5$ it gives $20+40=60$ degrees as required, and the temperature always decreases toward the room value without passing it.

### 4.5 Problem: a salt tank fed with brine

A tank holds $200$ litres of water with $2$ kilograms of salt dissolved in it. Brine containing $0.05$ kilograms of salt per litre enters at $4$ litres per minute, and the well-stirred mixture leaves at the same rate. Find the mass of salt after $60$ minutes, the mass after a very long time, and the concentration at that time.

### 4.6 Solution: balance the rates, then solve the linear equation

Step 1. Name the unknown. Let $Q$ be the mass of salt in the tank in kilograms at time $t$ in minutes.

Step 2. Compute the entry rate. Four litres per minute at $0.05$ kilograms per litre is $0.2$ kilograms per minute.

Step 3. Compute the exit rate. The tank holds $200$ litres at all times, so the concentration inside is $Q$ divided by $200$, and four litres per minute carries away $4\times\left(Q/200\right)=0.02Q$ kilograms per minute.

Step 4. Write the balance rule and the starting fact.

$$
\frac{dQ}{dt}=0.2-0.02Q , \qquad Q(0)=2
$$

Step 5. Solve. The equation is linear with constant coefficients, and its steady state is the value that makes the right side zero, namely $10$. The solution is the steady state plus a decaying exponential whose size is set by the starting value.

$$
Q=10-8e^{-0.02t}
$$

Step 6. Use the solution at $t=60$. The exponent is $1.2$ and the exponential is $0.30119$.

$$
Q=10-8\times 0.30119=10-2.41=7.59
$$

Step 7. State the long-run behaviour. As $t$ grows the mass tends to $10$ kilograms, and the concentration tends to $10$ divided by $200$, that is $0.05$ kilograms per litre, the strength of the incoming brine.

Step 8. Check the rule and the condition. The derivative of the answer is $0.16e^{-0.02t}$, and the right side is $0.2-0.02\left(10-8e^{-0.02t}\right)=0.2-0.2+0.16e^{-0.02t}$, which agrees. At $t=0$ the answer gives $10-8=2$ kilograms, as required, and the mass rises toward $10$ because the tank starts fresher than its inflow.

### 4.7 Problem: a coil switched on

A circuit in series contains a battery of $24$ volts, a resistance of $6$ ohms and an inductance of $0.5$ henries. The switch is closed at time zero, when the current is zero. Find the current at time $t$, the current after $0.1$ seconds, and the current after a long time.

### 4.8 Solution: divide by the inductance and use the standard answer

Step 1. Write Kirchhoff's voltage law for the loop.

$$
0.5\frac{di}{dt}+6i=24
$$

Step 2. Divide through by $0.5$ so that the coefficient of the derivative is one.

$$
\frac{di}{dt}+12i=48
$$

Step 3. Recognise the standard answer of Section 2.4: the final current is $48$ divided by $12$, which is $4$ amperes, and the time constant is $1$ divided by $12$ seconds.

$$
i=4\left(1-e^{-12t}\right)
$$

Step 4. Substitute $t=0.1$. The exponent is $1.2$ and the exponential is $0.30119$.

$$
i=4\left(1-0.30119\right)=4\times 0.69881=2.80
$$

Step 5. State the long-run current. It is $4$ amperes, which is the battery voltage divided by the resistance.

Step 6. Check. The derivative of the answer is $48e^{-12t}$, so the left side of the original equation is $0.5\times 48e^{-12t}+6\times 4\left(1-e^{-12t}\right)=24e^{-12t}+24-24e^{-12t}=24$, the battery voltage. The starting current is zero and the current rises without ever exceeding $4$ amperes.

### 4.9 Problem: a capacitor charging

A circuit in series contains a battery of $12$ volts, a resistance of $4$ ohms and a capacitance of one eighth of a farad. The capacitor is uncharged when the switch is closed. Find the charge and the current at time $t$, and the charge after one second.

### 4.10 Solution: the capacitive drop is the charge over the capacitance

Step 1. Write Kirchhoff's voltage law. The capacitor's drop is the charge divided by the capacitance, which is $8q$.

$$
4\frac{dq}{dt}+8q=12
$$

Step 2. Divide through by $4$.

$$
\frac{dq}{dt}+2q=3
$$

Step 3. Use the standard answer of Section 2.5. The final charge is $3$ divided by $2$, which is $1.5$ coulombs, and the time constant is $0.5$ seconds.

$$
q=1.5\left(1-e^{-2t}\right)
$$

Step 4. Differentiate to obtain the current.

$$
i=\frac{dq}{dt}=3e^{-2t}
$$

Step 5. Substitute $t=1$. The exponential is $0.13534$.

$$
q=1.5\left(1-0.13534\right)=1.5\times 0.86466=1.30
$$

Step 6. Interpret. The charge starts at zero and climbs to $1.5$ coulombs; the current starts at $3$ amperes and fades, and $3$ amperes is the battery voltage divided by the resistance, which is what Ohm's law gives at the first instant when the capacitor is still empty.

Step 7. Check. The derivative of the charge is $3e^{-2t}$, so $4\frac{dq}{dt}+8q=12e^{-2t}+12\left(1-e^{-2t}\right)=12$, and the starting charge is zero. The charge and the current are different quantities, and here the current is largest exactly when the charge is smallest.

### 4.11 Problem: an oscillating circuit without resistance

A circuit contains an inductance of $0.5$ henries and a capacitance of $0.02$ farads, with no resistance and no battery. Initially the capacitor holds $0.02$ coulombs and no current flows. Find the charge and the current at time $t$, the largest current, and the period of the oscillation.

### 4.12 Solution: a pure second-order oscillation

Step 1. Write the equation with the battery set to zero. The capacitor's drop is $q$ divided by $0.02$, which is $50q$.

$$
0.5\frac{d^{2}q}{dt^{2}}+50q=0
$$

Step 2. Divide by $0.5$ and read off the square of the angular frequency.

$$
\frac{d^{2}q}{dt^{2}}+100q=0
$$

Step 3. Write the general solution with angular frequency $10$ radians per second.

$$
q=A\cos\left(10t\right)+B\sin\left(10t\right)
$$

Step 4. Impose the starting charge. At $t=0$ the cosine is one and the sine is zero, so $A=0.02$.

Step 5. Differentiate to obtain the current and impose the starting current.

$$
i=-0.2\sin\left(10t\right)+10B\cos\left(10t\right)
$$

At $t=0$ this equals $10B$, which must be zero, so $B=0$.

Step 6. State the answers. The charge is $0.02\cos\left(10t\right)$ coulombs and the current is $-0.2\sin\left(10t\right)$ amperes. The largest current is $0.2$ amperes in size, and the period is $2\pi$ divided by $10$, about $0.628$ seconds.

Step 7. Check. Differentiating the charge twice multiplies it by $-100$, so the equation is satisfied; the starting charge is $0.02$ coulombs and the starting current is zero. The current is largest when the charge is zero, because the energy has moved entirely from the capacitor to the coil.

### 4.13 Problem: two trolleys released from a displaced position

For the two-trolley system of Section 1.8, the first trolley is pulled $1$ metre to the right, the second is left at its resting position, and both are released from rest. Find both displacements at time $t$.

### 4.14 Solution: combine the two rhythms and fit four conditions

Step 1. Recall the two rhythms found earlier, and write the general combination with unknown amounts $A$ and $C$ of each.

$$
x_1=A\cos t+2C\cos\left(\sqrt{6}\,t\right)
$$

$$
x_2=2A\cos t-C\cos\left(\sqrt{6}\,t\right)
$$

Step 2. Impose the starting displacements. The cosines are one at $t=0$.

$$
A+2C=1 , \qquad 2A-C=0
$$

Step 3. Solve the pair. The second equation gives $C=2A$, and the first then gives $5A=1$.

$$
A=\frac{1}{5} , \qquad C=\frac{2}{5}
$$

Step 4. Write the particular solution.

$$
x_1=\frac{1}{5}\cos t+\frac{4}{5}\cos\left(\sqrt{6}\,t\right)
$$

$$
x_2=\frac{2}{5}\cos t-\frac{2}{5}\cos\left(\sqrt{6}\,t\right)
$$

Step 5. Impose the starting velocities. Both answers are built from cosines only, so both velocities vanish at $t=0$, as required, and no further constant is needed.

Step 6. Check the first equation. Differentiating $x_1$ twice gives $-\frac{1}{5}\cos t-\frac{24}{5}\cos\left(\sqrt{6}\,t\right)$, and the combination $5x_1-2x_2$ is $\cos t+4\cos\left(\sqrt{6}\,t\right)-\frac{4}{5}\cos t+\frac{4}{5}\cos\left(\sqrt{6}\,t\right)$, which is $\frac{1}{5}\cos t+\frac{24}{5}\cos\left(\sqrt{6}\,t\right)$, exactly the negative of the acceleration. The first equation therefore holds.

Step 7. Check the second equation and the conditions. The combination $2x_1-2x_2$ equals $-\frac{2}{5}\cos t+\frac{12}{5}\cos\left(\sqrt{6}\,t\right)$, which is exactly the second derivative of $x_2$, so the second equation holds too; at $t=0$ the answer gives $x_1=1$ and $x_2=0$. Every condition is satisfied and four constants were fixed by four conditions.

## 5. Mathematical Extensions, Limits, and Common Errors

### 5.1 Where the simple models stop being true

Each of the five models rests on an assumption that is only approximately true, and knowing the assumption is part of knowing the mathematics.

The growth rule assumes that nothing limits the growth. Bacteria in a small dish eventually run out of food, and a population with limited resources grows quickly while it is small and then levels off. The simplest correction replaces the constant rate with a rate that falls as the population approaches its limit, giving the logistic rule $\frac{dx}{dt}=kx-\lambda x^{2}$, where $\lambda$ is a small positive number. The extra term is a brake that grows with the square of the population. Its solution still starts exponentially but bends over toward the value $k$ divided by $\lambda$, called the carrying capacity, and that value is the most useful thing to report in such a problem. The pure exponential is then the first approximation, valid while the population is far below the limit.

The mixture rule assumes that the tank is perfectly stirred, so that the liquid leaving has exactly the concentration of the tank as a whole. In a real tank the outflow may be drawn from a corner where the contents are richer or poorer than average. It also assumes that the tank does not overflow, which fails when the entry rate exceeds the exit rate: then the volume grows and the concentration is diluted by the growing volume as well as by the inflow. Both complications keep the equation linear, but the second makes the coefficient of $Q$ depend on time.

The circuit models assume that the resistance and the inductance are constants and that the battery voltage does not sag. Real coils have resistance of their own, and a real battery's voltage falls as it delivers current. The models also ignore the magnetic field of a changing current acting back on itself, an effect already contained in the inductance but only for a coil with no iron core. With iron the relation between current and flux is not proportional, and the equation becomes non-linear.

The two-spring model assumes Hooke's law, which says the force is proportional to the extension. Every real spring stops being proportional once it is stretched too far, and no spring can be compressed past its solid length. It also assumes no friction on the bench and no damping in the springs; with friction the two rhythms die away instead of repeating.

### 5.2 Beginner misconceptions

- **Thinking that the constant of proportionality is the answer.** In the growth problem the constant $k$ is not the population and not the growth; it is the growth per unit of population per unit of time. Answers must be given in the units of the quantity asked for, which for population is a number of individuals.
- **Writing the rate as a negative number and then adding a minus sign.** Choose one convention: keep $k$ positive and let the sign in front of it record growth or decay. Two minus signs cancel and turn a decaying substance into a growing one.
- **Treating a percentage rate as the constant $k$.** A growth of two per cent per year means a factor $1.02$ per year, so $k$ is the natural logarithm of $1.02$, not $0.02$. The difference is small but it is exactly what examiners test.
- **Using the inflow concentration in the outflow rate.** The liquid leaving the tank has the tank's concentration, which is the mass divided by the volume. This is the single most damaging error in mixture problems, and it usually produces an answer that never changes.
- **Forgetting the starting condition.** A general solution with an undetermined constant is not an answer to a word problem. The constant must be fixed, and the fixed value must be stated.
- **Adding the room temperature instead of subtracting it.** In the cooling rule the driving difference is the body's temperature minus the room's. If the body starts colder than the room it warms, and the same formula handles that case provided the difference is formed in the right order.
- **Confusing charge with current.** The charge is how much electricity has collected; the current is how fast it is collecting. In a capacitive circuit the charge rises while the current falls, and giving the charge as the current loses most of the marks.
- **Forgetting the second condition in a second-order problem.** Two constants need two facts. For a circuit these are usually the initial charge and the initial current, and for two trolleys they are the initial displacements and the initial velocities.
- **Assuming that more resistance always means slower return.** In the second-order circuit the effect of resistance is not monotone: a little resistance damps an oscillation and eventually removes it, but a great deal of resistance makes the return sluggish. The sign of $R^{2}-\frac{4L}{C}$ decides which behaviour occurs.
- **Believing that an exponential ever reaches its limit.** It does not. The temperature never equals the room temperature, the current never exactly equals its final value, and a graph that touches the limiting line has been drawn wrongly.
- **Losing the units.** A rate of $0.2$ has no meaning until it is $0.2$ kilograms per minute. Mixing litres and millilitres, or minutes and hours, is the commonest cause of a numerically absurd answer.

### 5.3 A checklist for any problem in this topic

1. Draw the situation in words, naming every quantity, its symbol and its unit.
2. State the physical law in one sentence, then translate that sentence into an equation.
3. Identify the order of the equation and therefore the number of conditions you will need.
4. Solve, keeping the constants until the conditions are imposed.
5. Impose the conditions and state the particular solution with its units.
6. Check by substitution, by the starting value, and by the long-run behaviour.
7. Write one sentence of interpretation that answers the question actually asked.

### 5.4 The five results worth remembering

The topic reduces to five formulas, each of which is the solution of one physical statement.

Growth and decay obey $x=x_0e^{kt}$ with $k$ positive for growth and negative for decay, and the doubling time or half-life is $\ln 2$ divided by the size of $k$.

Cooling obeys $T=T_s+\left(T_0-T_s\right)e^{-kt}$, so the excess over the room decays exponentially.

The well-stirred tank obeys $\frac{dQ}{dt}$ equal to the entry rate minus the product of the outflow rate and the tank concentration, and when the volume is constant the mass tends to the inflow concentration multiplied by the volume.

The first-order circuit obeys a solution of the form final value plus decaying exponential, with final current equal to the supply over the resistance for a coil and final charge equal to the capacitance times the supply for a capacitor.

The second-order circuit obeys a solution whose character is fixed by the sign of $R^{2}-\frac{4L}{C}$, and the two-spring system obeys a pair of equations whose solutions are combinations of two natural rhythms.

Every one of those sentences can be checked in a minute, and every one of them is a complete answer to a question worth several marks.
