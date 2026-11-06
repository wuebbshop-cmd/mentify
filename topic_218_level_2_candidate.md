## 1. Decision analysis: purpose and basic model

Decision analysis organizes a choice when its consequences depend on events that the decision maker cannot fully control. A useful model separates three things:

- **Decision alternatives (acts or strategies):** the actions available to the decision maker.
- **States of nature (events):** mutually exclusive situations that may occur but are not chosen by the decision maker.
- **Payoffs:** the gain, profit, cost, or loss that results from each alternative-state combination.

A payoff table puts alternatives in rows and states in columns. A cell contains the outcome if that row is selected and that column’s state occurs. Probabilities may be absent, producing a decision-under-uncertainty problem, or supplied, producing a decision-under-risk problem. The objective must also be explicit: maximize profit/payoff or minimize cost/time. Reversing the objective reverses the selection rule.

The approved module is organized as eleven lessons over eleven teaching weeks, followed by two revision weeks. The affected overview topic is therefore a map of the methods and their sequence, not a substitute for the calculations in each individual lesson.

## 2. The eleven-lesson sequence

The module plan builds from defining a problem to evaluating staged choices:

1. **Decision-making environment:** frame the problem, identify acts and possible events, and build the payoff representation.
2. **Decision making under uncertainty:** choose when state probabilities are unavailable, using attitudes such as optimism, pessimism, and Hurwicz’s compromise.
3. **Decision making under regret:** compare each payoff with the best payoff that could have been achieved in the same state, then control worst-case regret.
4. **Decision making under risk:** use supplied probabilities to calculate expected monetary value (EMV) and select the best expected payoff.
5. **Opportunity loss:** form an opportunity-loss table and choose by expected opportunity loss (EOL), where probabilities are available.
6. **Expected value under perfect information:** calculate the value of knowing the state before choosing an act and interpret the upper limit on information value.
7. **Relationship between EOL, EMV, and EVPI:** connect the expected-payoff and expected-loss calculations.
8. **Return-to-risk ratio:** add payoff variability to the comparison; EMV alone does not describe the spread of possible outcomes.
9. **Bayes’ decision analysis:** revise prior probabilities with a signal, then re-evaluate alternatives using posterior probabilities.
10. **Expected utility criterion:** represent a decision maker’s attitude toward risk when maximizing expected money does not capture preferences.
11. **Decision trees:** represent sequential choices and uncertain events, then evaluate the tree by working backward.

The sequence is cumulative. A payoff table supports several criteria; probability information enables EMV, EOL, and information-value calculations; a signal changes probabilities through Bayes’ rule; and a tree combines decisions and chance events across stages.

This progression also explains why the module separates its lessons. A decision problem can be represented once, then assessed through several different criteria without changing its underlying payoff table. The decision maker’s information and objective determine which calculation is appropriate. A state-probability distribution is not an alternative to the payoff table; it is additional information that can be used with the table. Similarly, a rating or forecast is not itself a state of nature. It is an observation that may change the probability assigned to the states.

The source’s weekly plan follows the same order: decision process (week 1), uncertainty (week 2), regret (week 3), risk (week 4), opportunity loss (week 5), perfect information (week 6), the EMV/EOL/EVPI relationship (week 7), return-to-risk ratio (week 8), Bayes (week 9), expected utility (week 10), and trees (week 11). Weeks 12 and 13 are reserved for examination. This is a useful revision map: if a question gives no probabilities, begin with the uncertainty lessons; if it gives probabilities, identify which risk, loss, or information criterion it asks for.

## 3. From an unstructured question to a payoff table

Before calculating, translate the narrative into a model. Ask:

1. What decision must be made now?
2. What alternatives are feasible, including a “do nothing” or status-quo option?
3. Which events affect the outcomes, and are they exhaustive and mutually exclusive?
4. What is the payoff in every cell, and is it profit, revenue, cost, or time?
5. Are probabilities supplied? Do they sum to one?
6. Is the requested objective to maximize or minimize?

For example, the module’s credit decision has two acts, extend credit or refuse credit, and states for the customer’s actual record. A payoff table forces the analyst to compare every act under every state instead of choosing from a single favorable outcome. Keep an alternative’s fixed cost separate until the cell payoffs are constructed, and avoid mixing gross revenue with net profit.

The credit example is especially useful for checking the structure. If a customer is actually a poor, average, or good credit risk, extending credit produces payoffs of -15,000, 10,000, or 20,000 monetary units. Refusing credit produces zero in every state. The prior probabilities are 0.2, 0.5, and 0.3:

| Actual credit state | Poor | Average | Good |
| --- | ---: | ---: | ---: |
| Extend credit | -15,000 | 10,000 | 20,000 |
| Refuse credit | 0 | 0 | 0 |
| Prior probability | 0.2 | 0.5 | 0.3 |

This one table can support more than one lesson. Without the probabilities, uncertainty criteria can be applied to the payoff rows. With the probabilities, the expected payoff from extending is

$$
0.2(-15{,}000)+0.5(10{,}000)+0.3(20{,}000)=8{,}000,
$$

while refusing has expected payoff zero. Later, if a rating organization supplies a signal, Bayes’ rule revises the state probabilities before the expected payoffs are compared. Keeping the original states and payoffs fixed makes it clear that the new evidence changes beliefs, not the underlying consequences.

## 4. Choosing a criterion for the information available

When no probabilities are known, the alternatives reflect different attitudes to the unknown. Maximax emphasizes the best possible result; maximin protects the best of the worst results; Hurwicz assigns a chosen optimism weight to each row’s best and worst payoff. Minimax regret instead asks how much payoff would be forgone after each state becomes known.

When probabilities are known, EMV weights each payoff by its state probability. EOL applies the same probabilities to regret values. EVPI measures the maximum expected benefit of learning the state before acting. These are averages across states, not guarantees about one realized outcome. Return-to-risk and expected utility add considerations that an expected-money average alone omits.

Use the following quick selection guide before calculating:

| Information or question wording | Suitable method | What is compared |
| --- | --- | --- |
| No state probabilities; best possible outcome | Maximax | Largest row maximum |
| No state probabilities; protect the worst payoff | Maximin | Largest row minimum |
| No state probabilities; intermediate optimism | Hurwicz | Weighted row maximum and minimum |
| Minimize worst missed payoff | Minimax regret | Smallest row maximum regret |
| State probabilities supplied; expected payoff requested | EMV | Largest probability-weighted row total |
| State probabilities supplied; expected foregone payoff requested | EOL | Smallest probability-weighted loss total |
| Worth of knowing the state perfectly | EVPI | EPPI minus best EMV, or minimum EOL |

The guide is not a substitute for reading the objective. For example, a probability row may appear in an exercise that asks specifically for maximin. In that part, use the requested maximin steps; use the probabilities only when the question asks for an expected-value calculation. Likewise, if an outcome is a cost, a minimum is preferable even though the same method’s payoff version may choose a maximum.

## 5. Information and staged decisions

A forecast or expert signal does not directly tell the decision maker which state will occur. Bayes’ theorem combines the prior state probabilities with the signal likelihoods to produce posterior probabilities. The decision maker then calculates each act’s conditional expected payoff and chooses the best act for that signal. A strategy may therefore prescribe different actions after different signals.

A decision tree is appropriate when one decision leads to a chance event and later decisions may follow. Decision nodes represent choices; chance nodes represent events with probabilities; terminal branches show final outcomes. Evaluate chance nodes by expected value and decision nodes by selecting the best available branch, rolling the calculation backward from the terminal outcomes.

Suppose a business can sell an asset now or keep it and decide later whether to operate it or sell after demand is observed. The first square is the sell-or-keep choice. The keep branch leads to a chance node for higher or lower demand. Each demand branch then leads to a second square because the business can make a new choice with that information. The correct policy can therefore be conditional: operate after high demand but sell after low demand. A one-row payoff table that assumes the same later action in both states would discard this flexibility.

The rollback calculation must also respect timing. A cost paid before the uncertain event is subtracted once from every relevant terminal payoff, or included in the branch payoffs from the outset. Do not subtract it again when taking the expectation. At each chance node, probabilities must be attached to outcomes at that node and sum to one. At each decision node, compare the rolled-back branch values using the same objective as the original problem.

## 6. Study and examination method

A strong answer makes the model visible. State the alternatives and states, show the payoff table, identify the criterion, show the row or column operation, and state the selected alternative with its value. When a question asks for a recommendation, interpret the number in context rather than reporting a criterion name alone.

Common errors across the module include treating a state of nature as an action, using probabilities that do not sum to one, maximizing a cost, taking a row maximum when a criterion requires a column comparison, mixing up EMV and EOL, and treating a posterior probability as a likelihood. In multi-stage questions, students often choose a locally attractive branch without rolling the entire tree back. A careful answer also flags inconsistent source arithmetic and recomputes from the displayed data before drawing a conclusion.

For revision, rehearse the same diagnostic sequence on every new problem: define the decision point; list controllable acts; list uncontrollable states; record the units and whether higher or lower is better; decide whether probabilities are available; identify the requested criterion; then calculate and interpret. If the problem contains a signal, add a separate probability-revision step before evaluating the action. If it contains more than one decision point, draw the sequence before calculating. This process prevents most method-selection errors and makes the working easy to mark.

The module’s source itself contains arithmetic inconsistencies in a few worked examples. Treat a printed conclusion as a claim to verify, not as a replacement for the supplied numbers. Recompute weighted sums, check that probability totals equal one, and test identities such as $EMV+EOL=EPPI$. If a source result does not reconcile, state the values shown, provide the corrected arithmetic, and explain whether the recommendation changes. This is part of sound decision analysis: the model should support the conclusion transparently.