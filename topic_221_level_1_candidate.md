## 1. What “decision under risk” means

Imagine choosing how many vegetable bags to order for a shop. You choose the number, but you do not choose how many customers will arrive. Ordering too few can miss sales; ordering too many can leave bags unsold. This familiar example shows the two parts of a decision problem: a choice you control and an event you do not.

A decision has alternatives: actions you can choose. It also has states of nature: things that may happen but are outside your control. Each action can lead to a different result depending on which state happens. The shop example is only an analogy for this structure; real decisions may involve many actions, states, and kinds of payoff.

Under **risk**, the problem gives probabilities for the states. A probability is a number from 0 to 1 that describes how likely an event is. For example, 0.2 means 20%. The probabilities for all the possible states should add to 1, or 100%.

This is different from the earlier “uncertainty” lesson. Under uncertainty, the probabilities are not known, so a person may choose an optimistic or cautious rule. Under risk, probabilities are available, so we can calculate an expected monetary value (EMV). EMV is a probability-weighted average payoff. It helps compare choices, but it does not promise that the average result will happen next time.

The word **risk** here does not simply mean that something bad will happen. It means that several outcomes are possible and the problem gives a probability for each one. The decision maker still cannot control which state occurs. The probabilities help compare choices; they do not let us choose the state.

## 2. Build the payoff table first

Before using a formula, write down:

- each decision you could make;
- each possible state of nature;
- the payoff for every combination;
- the probability of each state.

Keep the rows as actions and the columns as states. Check whether each number means profit, revenue, cost, or time. This matters because a larger profit is better, while a smaller cost or travel time is better.

The expected value process has three simple steps:

1. For one action, multiply each possible payoff by the probability of its state.
2. Add those weighted payoffs to get that action’s EMV.
3. Repeat for every action and select the best EMV for the goal.

For a payoff table,

$$
EMV(a)=\sum_j p_jx_{aj}.
$$

Here $p_j$ is the probability of state $j$, and $x_{aj}$ is the payoff for action $a$ if that state occurs. The formula just means “multiply each result by how likely it is, then add.” If the goal is to minimize cost, choose the smallest expected cost instead of the largest.

For example, the probability row $0.4,0.3,0.2,0.1$ means 40%, 30%, 20%, and 10%. The total is 1, or 100%, so the four states account for all possibilities. If the total were 0.9, a state or some probability mass would be missing. If the total were 1.2, at least one probability would have been entered incorrectly.

An expected value is not one of the table’s state outcomes. Only one state will occur on a particular occasion, while EMV averages the possible payoffs using their chances. Think of it as a fair comparison score for repeated similar decisions, not as a promise about tomorrow’s result.

## 3. Worked example: investing in bonds, stock, or deposits

The course example gives these annual returns:

| Choice | High growth | Medium growth | No change | Low growth |
| --- | ---: | ---: | ---: | ---: |
| Bonds | 12% | 8% | 7% | 3% |
| Stock | 15% | 5% | 5% | -2% |
| Deposits | 7% | 7% | 7% | 7% |
| Probability | 0.4 | 0.3 | 0.2 | 0.1 |

First check the probabilities: $0.4+0.3+0.2+0.1=1.0$. Now calculate one action at a time.

For bonds:

$$
EMV(B)=12(0.4)+8(0.3)+7(0.2)+3(0.1)=8.9\%.
$$

For stock:

$$
EMV(S)=15(0.4)+5(0.3)+5(0.2)+(-2)(0.1)=8.3\%.
$$

For deposits, every state gives 7%, so the expected return is also 7%. Bonds have the largest EMV, 8.9%, so bonds are the choice under this criterion.

This does not mean bonds must earn 8.9% in one year. The actual year will have one state, not an average of all four. EMV is useful for comparing choices over repeated or uncertain situations when the probabilities are reasonable.

The table also shows why the largest single payoff is not always the best choice by EMV. Stock can return 15% in high growth, but its lower returns in the other states reduce its weighted average to 8.3%. Deposits return the same 7% in every state, so their EMV is exactly 7%. Bonds do not have the largest payoff in every column, but their results combine to the highest expected return.

## 4. Worked example: how many vegetable bags to stock

A seller pays 8 dollars per bag and sells each bag for 10 dollars. Demand may be 10, 11, 12, 13, or 14 bags, with probabilities 0.1, 0.2, 0.4, 0.2, and 0.1. Unsold bags are discarded. Let $q$ be the number ordered and $d$ the number demanded.

If demand is at least the order, every ordered bag sells and profit is $2q$ dollars. If demand is below the order, only $d$ bags sell; revenue is $10d$ dollars and the cost is $8q$ dollars, so profit is $10d-8q$ dollars.

| Bags ordered | Demand 10 | 11 | 12 | 13 | 14 | EMV |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10 | 20 | 20 | 20 | 20 | 20 | 20.0 |
| 11 | 12 | 22 | 22 | 22 | 22 | 21.0 |
| 12 | 4 | 14 | 24 | 24 | 24 | 20.0 |
| 13 | -4 | 6 | 16 | 26 | 26 | 15.0 |
| 14 | -12 | -2 | 8 | 18 | 28 | 8.0 |

For 11 bags, multiply each payoff by the probability above its demand column:

$$
EMV(11)=0.1(12)+0.2(22)+0.4(22)+0.2(22)+0.1(22)=21.
$$

The largest expected profit is 21, so the seller should stock 11 bags. Ordering more raises profit when demand is high but risks paying for unsold bags. The calculation balances those possible outcomes using their probabilities.

Here is how to check individual cells. If the seller orders 12 bags and demand is only 10, two bags remain unsold. Revenue is 100 dollars and the cost of all 12 bags is 96 dollars, so profit is 4 dollars. If the seller orders 12 and demand is 14, all 12 ordered bags sell; profit is 12 times the 2-dollar margin, or 24 dollars. For an order of 14 when demand is 10, revenue is 100 dollars but cost is 112 dollars, so the result is a 12-dollar loss. The negative number is important: it shows why ordering too much can be risky.

Now calculate the row for ordering 11 bags one term at a time:

$$
0.1(12)+0.2(22)+0.4(22)+0.2(22)+0.1(22)
=1.2+4.4+8.8+4.4+2.2=21.
$$

The probabilities for demand 11, 12, 13, and 14 add to 0.9, so the payoff of 22 occurs with total probability 0.9. Only demand of 10 produces the 12 payoff. This is another quick way to check the arithmetic: $0.1(12)+0.9(22)=21$.

## 5. What the number tells you, and what it does not

Expected value summarizes both payoff size and probability. A large payoff in a very unlikely state may contribute less to EMV than a modest payoff in a common state. Likewise, a negative payoff must stay negative in the multiplication; changing its sign changes the decision.

EMV does not show how spread out the outcomes are. Two actions can have the same EMV but very different possible losses. A manager who is worried about variability may need a risk measure or expected-utility criterion as well. The course later introduces return-to-risk ratios and utility for these situations.

The quality of an EMV recommendation depends on the quality of the information used. If the probabilities come from past experience, ask whether the past situation is similar to the one being decided now. If the market has changed, older probabilities may no longer be a good guide. The calculation can be correct while the assumptions are weak. In a written answer, state that the recommendation follows from the supplied probabilities rather than claiming that those probabilities are certain facts.

The payoff itself also needs care. Use net profit when comparing profit choices. If a cost has already been subtracted in the payoff table, do not subtract it a second time. If the question gives only revenue but alternatives have different costs, revenue alone is not enough to decide which alternative is more profitable.

## 6. Exam steps and common mistakes

1. Write alternatives, states, payoffs, and probabilities in a table.
2. Check that the probabilities are between 0 and 1 and sum to 1.
3. Multiply each payoff by the probability for its column.
4. Add across each action’s row.
5. Choose the largest EMV for a profit goal or the smallest expected cost for a cost goal.
6. State the decision and what the expected value represents.

Common mistakes include weighting a payoff with the wrong state’s probability, leaving out a state, forgetting to include a negative payoff, averaging the payoffs without probabilities, and choosing a row by its best possible result rather than its EMV. Do not say that the EMV is guaranteed profit; it is a comparison measure, not a promise.

Before handing in an answer, ask yourself:

- Did I identify each action and each possible state correctly?
- Do the probabilities add to 1?
- Did I multiply every payoff by the probability at the top of its column?
- Did I keep losses negative and costs separate from revenue?
- Did I add across each action’s row?
- Did I choose the largest expected profit, or the smallest expected cost, as required?
- Did I explain that the expected value is an average comparison and not a guaranteed result?

The main idea is simple: write the possibilities clearly, give each possibility its proper weight, and compare the resulting averages. The careful setup is just as important as the multiplication.

When a decision repeats, record what actually happened and compare those outcomes with the probabilities used. If the observed pattern is very different over time, the probability estimates may need review. A single unexpected week does not by itself prove the probabilities were wrong; it is one possible outcome. This is another reason to treat EMV as a planning average, not as a promise.