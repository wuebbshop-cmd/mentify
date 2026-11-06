## 1. Bayes’ decision analysis and information

A decision maker may have prior probabilities for states of nature and then receive a signal, forecast, rating, or expert assessment. The signal does not reveal the state with certainty. Bayes’ decision analysis combines the prior probabilities with the signal’s accuracy to calculate posterior probabilities, then evaluates the alternatives using those revised probabilities.

Let $X$ be the state and $Y$ the observed signal. The posterior probability is

$$
P(X=x\mid Y=y)=\frac{P(X=x)P(Y=y\mid X=x)}{P(Y=y)},
$$

where the evidence probability is

$$
P(Y=y)=\sum_x P(X=x)P(Y=y\mid X=x).
$$

The numerator is prior times likelihood; the denominator adds the numerators over every possible state so the posterior probabilities sum to one.

## 2. Bayes’ workflow

1. List the mutually exclusive states and their prior probabilities.
2. List the possible signals and the likelihood of each signal conditional on each state.
3. For the signal actually observed, multiply each prior by its signal likelihood. These products are the joint probabilities for that signal and each state.
4. Add the joint probabilities to obtain the probability of observing the signal.
5. Divide each joint probability by that signal total to obtain the posterior probabilities.
6. Use the posterior probabilities with the payoff or cost table to calculate the conditional expected value of every decision alternative.
7. Select the alternative that matches the objective: highest expected profit or lowest expected cost.

A useful check is that the posterior probabilities for a given signal add to one. Do not confuse $P(Y\mid X)$, the probability of a signal if a state is true, with $P(X\mid Y)$, the revised probability of the state after seeing the signal.

## 3. Worked example: interest-rate signal

A broker can sell bonds now for a profit of USD 5,000 or wait six months. If she waits, profits and priors are:

| State | Prior probability | Profit from waiting | Probability of debt-raising signal given state |
| --- | ---: | ---: | ---: |
| Lower interest rates | 0.45 | 28,000 | 0.80 |
| No change | 0.35 | -5,000 | 0.20 |
| Higher interest rates | 0.20 | -15,000 | 0.10 |

Before the signal, the expected profit from waiting is

$$
0.45(28{,}000)+0.35(-5{,}000)+0.20(-15{,}000)=7{,}850.
$$

This exceeds the USD 5,000 available from selling immediately, so the prior-information decision is to wait.

For the debt-raising signal, the joint probabilities are $0.45(0.80)=0.36$, $0.35(0.20)=0.07$, and $0.20(0.10)=0.02$. Their sum, the probability of the signal, is 0.45. Thus the posterior probabilities are

$$
P(\text{lower}\mid signal)=0.36/0.45=0.800,
$$

$$
P(\text{no change}\mid signal)=0.07/0.45\approx0.156,
\qquad
P(\text{higher}\mid signal)=0.02/0.45\approx0.044.
$$

They sum to 1.000. Using the rounded posterior values, the expected profit from waiting after the signal is

$$
0.800(28{,}000)+0.156(-5{,}000)+0.044(-15{,}000)=20{,}960.
$$

Waiting remains preferable to selling immediately for USD 5,000. The module prints the prior expected profit as USD 7,800; its displayed payoffs and probabilities give USD 7,850. Use the calculated value and note the source discrepancy if quoting it.

## 4. Worked credit-rating example

A mill can extend credit or refuse. The actual customer state is poor, average, or good; prior probabilities are 0.2, 0.5, and 0.3. Extending credit has payoffs -15,000, 10,000, and 20,000 monetary units; refusing gives zero in every state. Without a rating signal,

$$
EMV(extend)=0.2(-15{,}000)+0.5(10{,}000)+0.3(20{,}000)=8{,}000.
$$

Therefore extending credit is preferred to refusing, whose EMV is zero.

The module also gives the chance of each rating conditional on the actual state:

| Rating signal | Poor actual record | Average actual record | Good actual record |
| --- | ---: | ---: | ---: |
| Poor | 0.50 | 0.40 | 0.20 |
| Average | 0.40 | 0.50 | 0.40 |
| Good | 0.10 | 0.10 | 0.40 |

For example, after a poor rating, the unnormalized joint weights are $0.2(0.50)=0.10$, $0.5(0.40)=0.20$, and $0.3(0.20)=0.06$. The signal probability is 0.36, so the posterior state probabilities are approximately 0.278, 0.556, and 0.167. Using the unrounded posterior ratios, the conditional expected payoff from extending is about

$$
\frac{0.10}{0.36}(-15{,}000)+\frac{0.20}{0.36}(10{,}000)+\frac{0.06}{0.36}(20{,}000)\approx4{,}722.
$$

It remains positive, so extending credit is preferred even after a poor rating in this example. The key is to calculate the posterior before applying the payoff criterion; a rating label is evidence, not the state itself.

The other two rating signals can be calculated the same way. For an average rating, the joint weights are $0.2(0.40)=0.08$, $0.5(0.50)=0.25$, and $0.3(0.40)=0.12$. The signal probability is 0.45, giving posterior probabilities 0.178, 0.556, and 0.267. For a good rating, the joint weights are 0.02, 0.05, and 0.12; the signal probability is 0.19, giving posteriors 0.105, 0.263, and 0.632.

| Observed rating | Signal probability | Posterior poor | Posterior average | Posterior good | Expected payoff from extending |
| --- | ---: | ---: | ---: | ---: | ---: |
| Poor | 0.36 | 0.278 | 0.556 | 0.167 | 4,722 |
| Average | 0.45 | 0.178 | 0.556 | 0.267 | 8,222 |
| Good | 0.19 | 0.105 | 0.263 | 0.632 | 13,684 |

Refusing credit has expected payoff zero after every rating. Extending credit has a positive expected payoff after all three ratings, so the optimal action does not change. The signal still changes the expected value of the credit decision, but it does not change the chosen action in this particular example. The probability of each rating and its posterior state probabilities are separate quantities; the first is used to weight decisions across possible signals, while the second is used to choose an action after one signal is observed.

If the rating is observed before the credit decision, the expected profit of the resulting strategy is

$$
0.36(4{,}722.22)+0.45(8{,}222.22)+0.19(13{,}684.21)\approx8{,}000.
$$

That equals the prior expected profit because the signal never changes the action. In decision terms, the signal has zero expected value here, even though it provides information about the customer’s likely state. Information is valuable for a decision only when it can improve the choice or its expected consequence.

The posterior decision rule can be written as a threshold. Let $q_P$, $q_A$, and $q_G$ be the posterior probabilities of poor, average, and good actual credit. Extending is preferred when

$$
-15{,}000q_P+10{,}000q_A+20{,}000q_G>0,
$$

or, after dividing by 5,000, when $-3q_P+2q_A+4q_G>0$. This makes the decision boundary visible: a signal changes the act only if its posterior probabilities move the expected payoff across zero. If extending and refusing have the same expected payoff, the decision maker is indifferent under EMV and may use a stated secondary rule.

## 5. Decision under a forecast and data consistency

A signal’s value depends on how accurately it predicts each state and on the consequences of the available actions. A strong signal can still fail to change the decision if one act remains best under all posterior distributions. Conversely, an imperfect signal can be useful when the posterior expected values cross the decision threshold.

The module’s carpool example gives prior traffic-jam probability 0.15 and a time table. Its displayed expected times are 30 minutes for Juja and 28 minutes for Thika, which favors Thika when minimizing time, although the printed conclusion says Juja. For the Bayes extension, additional conditional weather probabilities are needed; some supplied conditional values are incomplete or inconsistent. Do not manufacture a posterior from missing likelihoods. State the inconsistency and use only a coherent set of probabilities.

The initial expected-time calculation is:

$$
E(T_{Juja})=0.85(30)+0.15(30)=30\text{ minutes},
$$

$$
E(T_{Thika})=0.85(25)+0.15(45)=28\text{ minutes}.
$$

Since the objective is to minimize travel time, Thika is preferred before the extra weather information is considered. This is a useful directional check: when lower values are better, the decision rule selects the smaller expected value. The source’s printed recommendation of Juja conflicts with its own table totals.

After a signal is observed, do not stop at the posterior probabilities. Calculate the expected time or payoff of every action using those posterior weights, then select the best conditional action. A complete strategy may say “take Thika after one signal and Juja after another.” If the available conditional probabilities do not determine the signal likelihoods or the state posterior, the strategy cannot be completed without additional information.

Posterior tables have a consistency check: when all possible signals are considered, weighting each signal-specific posterior by that signal’s probability recovers the original prior. In notation, $\sum_yP(y)P(x\mid y)=P(x)$. This follows from the joint probabilities and helps catch a signal row normalized with the wrong denominator. It does not mean the posterior equals the prior after one particular signal; it means the prior is recovered when averaging across all possible signals before knowing which one occurs.

## 6. Examination checklist and common errors

- Identify the direction of conditioning in every probability.
- Multiply prior by likelihood to form joint weights.
- Divide by the signal total to normalize; check the posterior sum is 1.
- Recompute expected payoff or expected cost under the posterior, not the prior.
- Compare against all available alternatives, including “sell now” or “do nothing.”
- Separate source arithmetic from source conclusions when they disagree.

Frequent errors include using the likelihood as a posterior, normalizing by the wrong signal total, forgetting an outcome, multiplying a payoff by a prior after observing the signal, treating an imperfect forecast as certainty, and copying inconsistent printed totals. Show the prior, likelihood, joint, and posterior columns so the reasoning can be audited.