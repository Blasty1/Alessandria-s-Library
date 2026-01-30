>[!SUMMARY] Table of Contents
- [[Reinforcement Learning Basic Course#Introduction of RL|Introduction of RL]]
    - [[Reinforcement Learning Basic Course#Inside an RL agent|Inside an RL agent]]
    - [[Reinforcement Learning Basic Course#Maze Example|Maze Example]]
- [[Reinforcement Learning Basic Course#Markov Decision Process|Markov Decision Process]]
    - [[Reinforcement Learning Basic Course#Markov Property|Markov Property]]
    - [[Reinforcement Learning Basic Course#Markov Process|Markov Process]]
    - [[Reinforcement Learning Basic Course#Markov Reward Process MRP|Markov Reward Process MRP]]
    - [[Reinforcement Learning Basic Course#Value Function|Value Function]]
    - [[Reinforcement Learning Basic Course#Bellman Equation for MRPs|Bellman Equation for MRPs]]
    - [[Reinforcement Learning Basic Course#Markov Decision Process MDP|Markov Decision Process MDP]]
        - [[Reinforcement Learning Basic Course#Stochastic Policy|Stochastic Policy]]
        - [[Reinforcement Learning Basic Course#Value function|Value function]]
        - [[Reinforcement Learning Basic Course#Bellman Expectation Equation|Bellman Expectation Equation]]
        - [[Reinforcement Learning Basic Course#Optimal Value Function|Optimal Value Function]]
        - [[Reinforcement Learning Basic Course#Optimal Policy|Optimal Policy]]
        - [[Reinforcement Learning Basic Course#Bellman Optimality Equation|Bellman Optimality Equation]]
        - [[Reinforcement Learning Basic Course#Solving the Bellman Optimality Equation|Solving the Bellman Optimality Equation]]
- [[Reinforcement Learning Basic Course#Planning by Dynamic Programming|Planning by Dynamic Programming]]
    - [[Reinforcement Learning Basic Course#Policy Evaluation|Policy Evaluation]]
    - [[Reinforcement Learning Basic Course#Policy Iteration|Policy Iteration]]
        - [[Reinforcement Learning Basic Course#Modified Policy Iteration|Modified Policy Iteration]]
    - [[Reinforcement Learning Basic Course#Value Iteration Algorithm|Value Iteration Algorithm]]
        - [[Reinforcement Learning Basic Course#Summary of Synchronous Dynamic Programming Algorithm|Summary of Synchronous Dynamic Programming Algorithm]]
    - [[Reinforcement Learning Basic Course#Extensions to DP|Extensions to DP]]
        - [[Reinforcement Learning Basic Course#Asynchronous DP|Asynchronous DP]]
        - [[Reinforcement Learning Basic Course#Full-Width and Sample Backups|Full-Width and Sample Backups]]
- [[Reinforcement Learning Basic Course#Model-free Prediction|Model-free Prediction]]
    - [[Reinforcement Learning Basic Course#Monte-Carlo Learning|Monte-Carlo Learning]]
        - [[Reinforcement Learning Basic Course#First-Visit Monte-Carlo Policy Evaluation|First-Visit Monte-Carlo Policy Evaluation]]
        - [[Reinforcement Learning Basic Course#Every-Visit Monte-Carlo Policy Evaluation|Every-Visit Monte-Carlo Policy Evaluation]]
    - [[Reinforcement Learning Basic Course#Temporal-Difference Learning|Temporal-Difference Learning]]
    - [[Reinforcement Learning Basic Course#Batch MD and TD|Batch MD and TD]]
    - [[Reinforcement Learning Basic Course#MC vs TD|MC vs TD]]
    - [[Reinforcement Learning Basic Course#MC vs TD vs DP backups|MC vs TD vs DP backups]]
    - [[Reinforcement Learning Basic Course#Bootstrapping and Sampling|Bootstrapping and Sampling]]
    - [[Reinforcement Learning Basic Course#TD($\lambda$)|TD($\lambda$)]]
        - [[Reinforcement Learning Basic Course#$\lambda-$Return|$\lambda-$Return]]
        - [[Reinforcement Learning Basic Course#Forward-view TD($\lambda$)|Forward-view TD($\lambda$)]]
        - [[Reinforcement Learning Basic Course#Backward-view TD($\lambda$)|Backward-view TD($\lambda$)]]
    - [[Reinforcement Learning Basic Course#TD(0) and TD($\lambda$)|TD(0) and TD($\lambda$)]]
    - [[Reinforcement Learning Basic Course#Summary of Forward and Backward TD($\lambda$ )|Summary of Forward and Backward TD($\lambda$ )]]
- [[Reinforcement Learning Basic Course#Model Free Control|Model Free Control]]
    - [[Reinforcement Learning Basic Course#On-Policy Monte-Carlo Control|On-Policy Monte-Carlo Control]]
        - [[Reinforcement Learning Basic Course#Generalised Policy Iteration GPI|Generalised Policy Iteration GPI]]
        - [[Reinforcement Learning Basic Course#Generalised Policy Iteration with MC Evaluation|Generalised Policy Iteration with MC Evaluation]]
        - [[Reinforcement Learning Basic Course#GLIE Monte-Carlo Control|GLIE Monte-Carlo Control]]
    - [[Reinforcement Learning Basic Course#On-Policy Temporal Difference Learning|On-Policy Temporal Difference Learning]]
        - [[Reinforcement Learning Basic Course#Updating Action-Value Functions with Sarsa|Updating Action-Value Functions with Sarsa]]
        - [[Reinforcement Learning Basic Course#n-Step Sarsa|n-Step Sarsa]]
    - [[Reinforcement Learning Basic Course#Off-Policy Learning|Off-Policy Learning]]
        - [[Reinforcement Learning Basic Course#Importance Sampling|Importance Sampling]]
        - [[Reinforcement Learning Basic Course#Q-Learning|Q-Learning]]
        - [[Reinforcement Learning Basic Course#Relationship between DP and TD|Relationship between DP and TD]]
- [[Reinforcement Learning Basic Course#Value Function Approximation|Value Function Approximation]]
    - [[Reinforcement Learning Basic Course#Incremental methods|Incremental methods]]
        - [[Reinforcement Learning Basic Course#Gradient Descent|Gradient Descent]]
        - [[Reinforcement Learning Basic Course#Linear Function Approximation|Linear Function Approximation]]
        - [[Reinforcement Learning Basic Course#Incremental Prediction Algorithm|Incremental Prediction Algorithm]]
            - [[Reinforcement Learning Basic Course#Monte Carlo with Value Function Approximation|Monte Carlo with Value Function Approximation]]
            - [[Reinforcement Learning Basic Course#TD  Learning with Value Function Approximation|TD  Learning with Value Function Approximation]]
            - [[Reinforcement Learning Basic Course#TD($\lambda$)  Learning with Value Function Approximation|TD($\lambda$)  Learning with Value Function Approximation]]
        - [[Reinforcement Learning Basic Course#Incremental Control Algorithm|Incremental Control Algorithm]]
            - [[Reinforcement Learning Basic Course#Action-Value Function Approximation|Action-Value Function Approximation]]
            - [[Reinforcement Learning Basic Course#Linear Action-Value Function Approximation|Linear Action-Value Function Approximation]]
        - [[Reinforcement Learning Basic Course# Convergence of prediction algorithms | Convergence of prediction algorithms ]]
        - [[Reinforcement Learning Basic Course#Gradient Temporal-Difference Learning|Gradient Temporal-Difference Learning]]
        - [[Reinforcement Learning Basic Course#Convergence of Control Algorithms|Convergence of Control Algorithms]]
- [[Reinforcement Learning Basic Course#Batch Methods|Batch Methods]]
    - [[Reinforcement Learning Basic Course#Least Square Prediction|Least Square Prediction]]
        - [[Reinforcement Learning Basic Course#Experience Replay in Deep Q-Networks|Experience Replay in Deep Q-Networks]]
        - [[Reinforcement Learning Basic Course#Linear Least Squares Prediction Algorithms|Linear Least Squares Prediction Algorithms]]
    - [[Reinforcement Learning Basic Course#Least Square Control|Least Square Control]]
        - [[Reinforcement Learning Basic Course#Least Squares Policy Iteration|Least Squares Policy Iteration]]
        - [[Reinforcement Learning Basic Course#Least Square Q-learning|Least Square Q-learning]]
        - [[Reinforcement Learning Basic Course#Least Squares Policy Iteration Algorithm|Least Squares Policy Iteration Algorithm]]
- [[Reinforcement Learning Basic Course#Policy Gradient|Policy Gradient]]
    - [[Reinforcement Learning Basic Course#Policy-Based RL|Policy-Based RL]]
    - [[Reinforcement Learning Basic Course#RL Categorization|RL Categorization]]
    - [[Reinforcement Learning Basic Course#Policy Evaluation through Policy Objective Functions|Policy Evaluation through Policy Objective Functions]]
    - [[Reinforcement Learning Basic Course#Policy Optimization|Policy Optimization]]
    - [[Reinforcement Learning Basic Course#Finite Difference Policy Gradient|Finite Difference Policy Gradient]]
    - [[Reinforcement Learning Basic Course#Monte Carlo Policy Gradient|Monte Carlo Policy Gradient]]
        - [[Reinforcement Learning Basic Course#Policy Gradient Theorem|Policy Gradient Theorem]]
        - [[Reinforcement Learning Basic Course#Monte Carlo Policy Gradient Algorithm|Monte Carlo Policy Gradient Algorithm]]
    - [[Reinforcement Learning Basic Course#Actor-Critic Policy Gradient|Actor-Critic Policy Gradient]]
        - [[Reinforcement Learning Basic Course#Action-Value Actor-Critic|Action-Value Actor-Critic]]
        - [[Reinforcement Learning Basic Course#Estimating the Advantage Function|Estimating the Advantage Function]]
        - [[Reinforcement Learning Basic Course#Critics at Different Time-Scales|Critics at Different Time-Scales]]
        - [[Reinforcement Learning Basic Course#Natural Policy Gradient|Natural Policy Gradient]]
    - [[Reinforcement Learning Basic Course#Summary of Policy Gradient Algorithms|Summary of Policy Gradient Algorithms]]
- [[Reinforcement Learning Basic Course#Integrating Learning and Planning|Integrating Learning and Planning]]
    - [[Reinforcement Learning Basic Course#Model-Based Reinforcement Learning|Model-Based Reinforcement Learning]]
        - [[Reinforcement Learning Basic Course#Learning a Model|Learning a Model]]
            - [[Reinforcement Learning Basic Course#Table Lookup Model|Table Lookup Model]]
        - [[Reinforcement Learning Basic Course#Planning with a Model|Planning with a Model]]
            - [[Reinforcement Learning Basic Course#Sample-Based Planning|Sample-Based Planning]]
            - [[Reinforcement Learning Basic Course#Planning with an Inaccurate Model|Planning with an Inaccurate Model]]
    - [[Reinforcement Learning Basic Course#Integrated Architectures|Integrated Architectures]]
        - [[Reinforcement Learning Basic Course#Dyna Architecture|Dyna Architecture]]
    - [[Reinforcement Learning Basic Course#Simulation-Based Search|Simulation-Based Search]]
        - [[Reinforcement Learning Basic Course#Forward Search|Forward Search]]
        - [[Reinforcement Learning Basic Course#Simple Monte-Carlo Search|Simple Monte-Carlo Search]]
        - [[Reinforcement Learning Basic Course#Monte-Carlo Tree Search|Monte-Carlo Tree Search]]
                - [[Reinforcement Learning Basic Course#Example Game of Go|Example Game of Go]]
        - [[Reinforcement Learning Basic Course#TD Search|TD Search]]
            - [[Reinforcement Learning Basic Course#Dyna-2|Dyna-2]]
- [[Reinforcement Learning Basic Course#Exploration and Exploitation|Exploration and Exploitation]]
    - [[Reinforcement Learning Basic Course#Multi-armed bandit|Multi-armed bandit]]
        - [[Reinforcement Learning Basic Course#Regret|Regret]]
        - [[Reinforcement Learning Basic Course#Greedy Algorithm|Greedy Algorithm]]
        - [[Reinforcement Learning Basic Course#$\epsilon-$Greedy Algorithm|$\epsilon-$Greedy Algorithm]]
        - [[Reinforcement Learning Basic Course#Decaying $\epsilon_t -$Greedy Algorithm|Decaying $\epsilon_t -$Greedy Algorithm]]
        - [[Reinforcement Learning Basic Course#Lower Bound|Lower Bound]]
        - [[Reinforcement Learning Basic Course#Upper Confidence Bound UCB|Upper Confidence Bound UCB]]
            - [[Reinforcement Learning Basic Course#Hoeffding's Inequality|Hoeffding's Inequality]]
            - [[Reinforcement Learning Basic Course#Calculate UCB|Calculate UCB]]
            - [[Reinforcement Learning Basic Course#UCB1 Algorithm|UCB1 Algorithm]]
        - [[Reinforcement Learning Basic Course#Bayesian Bandits |Bayesian Bandits ]]
            - [[Reinforcement Learning Basic Course#Bayesian UCB|Bayesian UCB]]
            - [[Reinforcement Learning Basic Course#Thompson Sampling|Thompson Sampling]]
        - [[Reinforcement Learning Basic Course#Information State Search|Information State Search]]
        - [[Reinforcement Learning Basic Course#Summary|Summary]]
$$
\newcommand{\argmax}{\text{arg max}}
$$
$$
\newcommand{\w}{\textbf{w}}
$$
# Introduction of RL

Reinforcement learning is studying the science of decision making which makes it very general.

Reinforcement learning is different from other machine learning paradigms because:
1. There is no supervisor, only reward signal ( bad/good behavior , but not quantification of it like how much bad it was)

2. The feedback is not instantaneous, it can be delayed from a set of steps

3. Times really matters in RL ( it is a set of sequential steps , we don’t have i.i.d data as in the supervised classical problems )

4. There is an agent(e.g. a robot ) moving through the world

5. The agent is influencing the data that he is actually seeing ( he moves in the world that he is studying we can say )

A reward is a scalar feedback signal ( a number ) that says how well is the agent doing at that time step $R_t$. The job of the agent is to sum up these rewards and get as much reward as possible in total.

> All goals can be described by the maximisation of expected cumulative reward

>

  

For different types of problem the goal is the same: we want to selects actions that maximise total future reward.

  

Reward can be delayed so we should think ahead: it is possible that we need to sacrifice immediate reward to gain more long-term reward.

  

![IMG_7049341E3E40-1.jpeg](images/IMG_7049341E3E40-1.jpeg)

  

Our goal is to build this brain which represents the agent:

  

![IMG_970E942AF35E-1.jpeg](images/IMG_970E942AF35E-1.jpeg)

  

The world is the environment.

  

The **history** is what the agent has been seen so far: a sequence of observations, actions and rewards

  

$$

H_t = O_1 , R_1 , A_1 , ... , A_{t-1} , O_t , R_t

$$

  

These are all the **observable variables** up to time t ( the things that are not exposed to our agent can not be taken into consideration for building a correct algorithm and they should be ignored ).

  

Our algorithm is just a mapping from the history to the next action.

  

**State** is a function of the history used to determine what happens next:

  

$$

S_t = f(H_t)

$$

  

We have 3 different definitions of state:

  

1. Environment state $S_t^e$ : information used within the environment to determine what happens next.

2. It is not visible to the agent and it does not give us any relevant information for building up our algorithm

  

![IMG_49077EBAB63F-1.jpeg](images/IMG_49077EBAB63F-1.jpeg)

  

1. Agent state $S_t^a$ : information that summarize what happens so far used by the agent to pick the next action.

2. It is the information by RL algorithms

3. It can be any function of history $S_t^a = f(H_t)$

  

![IMG_1569575E4969-1.jpeg](images/IMG_1569575E4969-1.jpeg)

  

1. Information state / Markov State : it contains all useful information from the state ( it is a much more mathematical concept )

2. A state is Markov if it satisfies the **markov property** ( the future is independent of the past given the present )

  

$$

P[S_{t+1} | S_t ] = P[S_{t+1} | S_1 , . . . , S_t ]

$$

  

We can throw away the history once the state is known ( the state is a sufficient statistic of the future ).

  

Both environment and history are Markov states.

  

The environment can be:

  

- Fully observable → agent directly observers environment state

  

$$

O_t = S_t^a = S_t^e

$$

  

The observation is equal to the state of the environment and to the state of the agent.

  

This is a Markov Decision Process ( MDP ).

  

It is the nicest case.

  

- Partially observable → agent indirectly observes environment

  

$$

S_t^a \neq S_t^e

$$

  

This is a partially observable Markov Decision Process ( PO-MDP )

  

The agent must construct its own state representation $S_t^a$ , it can:

  

1. Use the whole history $S_t^a = H_t$

2. Build a beliefs of environment state ( bayesian approach ) → i keep probability distribution of where i am in the environment

$S_t^a = (P[S_t^e = s^1] , . . . , P[S_t^e = s^n])$

3. Recurrent neural network ( linear combination between the previous agent state and the current observation )

$S_t^a = \sigma(S^a_{t-1} W_s + O_t W_o)$

  

## Inside an RL agent

  

RL agent may include one or more of these components:

  

1. Policy → how the agent picks its actions , its behaviour function.

  

It is a map from state to action , it can be

  

- Deterministic → $a = \pi(s)$

- Stochastic → $\pi(a|s) = P[A_t=a| S_t = s]$

1. Value function → how good is it to be in a particular state or how much reward i get to perform a specific action

  

It is a prediction of future reward and it is used to select between actions

  

![image.png](images/image.png)

  

It says how much reward the agent will get if it continues to follow the current set of actions.

  

1. Model → how the agent thinks the environment works

2. It is not the really environment but just the agent’s view of it

3. It is a prediction of what the environment will do next

  

![IMG_878197AEA5AB-1.jpeg](images/IMG_878197AEA5AB-1.jpeg)

  

$P$ predicts the next state

  

$R$ predicts the next reward

  

## Maze Example

  

This is the problem that we want to solve:

  

![Screenshot 2026-01-12 alle 18.05.28.png](images/Screenshot_2026-01-12_alle_18.05.28.png)

  

We want to find the path to got outside the maze.

  

We need to define:

  

- Policy → a deterministic policy can be a set of pre-defined movements that the agent has to do when he is in a specific position.

![Screenshot 2026-01-12 alle 18.06.40.png](images/Screenshot_2026-01-12_alle_18.06.40.png)

- Value Function → we give numbers to each position, the next action will be the one that minimizes it.

![Screenshot 2026-01-12 alle 18.07.32.png](images/Screenshot_2026-01-12_alle_18.07.32.png)

- Model → how the agent thinks the environment is

![Screenshot 2026-01-12 alle 18.08.18.png](images/Screenshot_2026-01-12_alle_18.08.18.png)

  

Numbers represent immediate reward $R_s^a$ from each state s.

  

We can categorize our RL agents using this 3 components:

  

- It is a **value based** agent if it contains a value function and the policy becomes/is implicit.

- It is a **policy based** agent if we explicitly represent the policy without using the value function.

- **Actor critic** is an agent that uses both policy and value function.

  

An RL agent can be

  

- Model Free → we don’t try to explicit understand the environment ( no model )

- Model based

  

![intro_rl-36.jpg](images/f9fb3246-2ca8-4f81-9f75-e1bf6f74851a.png)

  

There are 2 problems related to sequential decision making:

  

1. Reinforcement Learning problem:

2. The environment is initially unknown

3. The agent interacts with the environment and it improves its policy

4. Planning problem

5. A model of the environment is known (e.g. the rules of a game )

6. The agent does not interact with the external environment but it performs computations with its model improving its policy.

  

RL learning is a *trial-and-error* learning: we want to find a good policy from its experience of the past without loosing too much reward along the way.

  

We want to find a balance between:

  

- Exploration → finds more information about the environment giving up some rewards we know about

- Exploitation → exploits the information you already found to maximise reward

  

![image.png](images/image%201.png)

  

We must also highlight a distinction between:

  

- Prediction → it evaluates the future given a policy

  

![image.png](images/image%202.png)

  

- Control → it optimises the future ( it finds the best policy )

  

![image.png](images/image%203.png)

  

# Markov Decision Process

  

MDP is the formal description of an environment for RL where the environment is fully observable ( the current state is fully observable ).

  

All the RL problems can be formalised as MDPs.

  

## Markov Property

  

The future is independent from the past given the present

  

![image.png](images/image%204.png)

  

The state captures all relevant information from the history

  

The probability of moving from a state s to the a successor state s’ is called **state transition probability:**

  

$$

P_{ss'}=P[S_{t+1} = s' | S_t = s]

$$

  

We can define the **state transition matrix $P$** that considers all the combinations:

  

![image.png](images/image%205.png)

  

Each row of the matrix sums to 1 ( given a state , all the possible next choice probabilities must sum to 1 ).

  

## Markov Process

  

A markov process is a memoryless random process: a sequence of random states $S_1 , S_2 , . . .$ with the Markov Property

  

![image.png](images/image%206.png)

  

Example of student markov chain with its transition probability matrix

  

![image.png](images/image%207.png)

  

## Markov Reward Process MRP

  

A Markov reward process is a Markov chain with values

  

![image.png](images/image%208.png)

  

The reward function tells us how much reward we get if we stay in a state $S_t = s$ ( immediate reward ).

  

Let’s see our example of the student MRP

  

![image.png](images/image%209.png)

  

⚠️ when we leave a state we will obtain the specified reward independetly from the next state.

  

e.g. when i leave the state class 1 i will get always R=-2.

  

The goal of the Reinforcement Learning is to maximise the return $G_t$ which is the total discounted reward from time-step t

  

$$

G_t = R_{t+1} + \gamma R_{t+1} + . . . = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}

$$

  

$R_{t+1}$ is the immediate reward and then we have the future rewards discounted properly: the discount is $\gamma \in [0,1]$ and it tells how much i care now about rewards i’ll get in the future.

  

$\gamma$ is more about *how much you value* future rewards, not necessarily how much you *trust* your predictions:

  

- If $\gamma = 0$ means you're completely myopi ( you only care about the immediate reward $R_{t+1}$) Future rewards literally don't factor into your decision at all. It's not that you don't trust your predictions; you simply don't care about the future.

- Myopic evaluation

- If $\gamma = 1$ means you value a reward 100 steps from now exactly as much as a reward right now. There's no discounting at all—every future reward counts equally.

- Far-sighted evaluation

  

We are weighting the importance of future reward in our decision.

  

Why Markov reward and decision processes are discounted?

  

- Mathematically convenient ( the sum to $\infty$ will converge )

- Future is uncertain because we do not have a perfect model of the environment

- We can also use undiscounted Marko reward processes ( i.e. $\gamma = 1$ ) if all sequences terminate

  

## Value Function

  

The value function $v(s)$ is the long-term value of being in the state s

  

![image.png](images/image%2010.png)

  

In other words, what is the total reward that you will get from this state on.

  

Let’s go back to the example of Student MRP and we will analyze the sample returns for it:

  

![image.png](images/image%2011.png)

  

Each row is a sample, each sample represents a different sequence of steps.

  

Let’s see several examples of the value function with different discount values:

  

![image.png](images/image%2012.png)

  

We take into account only the immediate reward, in other words $v(s) = E[R_{t}]$

  

![image.png](images/image%2013.png)

  

![image.png](images/image%2014.png)

  

## Bellman Equation for MRPs

  

The value function can be decomposed into two parts:

  

1. Immediate rewards $R_{t+1}$

2. Discounted value of successor state $\gamma v(S_{t+1})$

  

![image.png](images/image%2015.png)

  

Bellman equation is then

  

$$

v(s) = E[ R_{t+1} + \gamma v(S_{t+1}) | S_t = s ]

$$

  

We can represent it using the backup diagram which is a one-step look ahead search

  

![image.png](images/image%2016.png)

  

$$

v(s) = R_s + \gamma \sum_{s' \in S} P_{ss'} v(s')

$$

  

We get the value function at this step by averaging all the possible outcomes together.

  

In particular:

  

The summation $\sum_{s' \in S} P_{ss'} v(s')$ is computing an **expectation : we**'re weighting each possible next state's value $v(s')$ by the probability $P_{ss'}$ of actually transitioning there, then summing them all up.

  

Computation example:

  

![image.png](images/image%2017.png)

  

We have just selected one state: the red one.

  

We can express the bellman equation using matrices:

  

$$

v = R + \gamma P v

$$

  

![image.png](images/image%2018.png)

  

Where:

  

- v is a column vector with one entry per state.

- R is a column vector where each entry tells how much reward i get by exiting that state.

  

Bellman equation in this case is a linear equation so it can be solved directly:

  

![image.png](images/image%2019.png)

  

Its complexity is $O(n^3)$ where n is the number of states.

  

This is an usable solution only for small MRPs, but for large MRPs we shall use iterative methods:

  

- Dynamic programming

- Monter-Carlo evaluation

- Temporal-Difference learning

  

## Markov Decision Process MDP

  

It is a Markov reward process MRP with decisions. It is an environment in which all states are Markov.

  

![image.png](images/6f9b9e95-6ad2-4bb8-bc74-d2813282dd04.png)

  

The reward function now depends both on the state and on which type of action we take.

  

We just need to consider actions: the transition probability matrix depends on which action we take; in a discrete context, we have a different state transition probability for each action $a$.

  

![image.png](images/image%2020.png)

  

The decisions are the red strings on the arcs

  

### Stochastic Policy

  

A policy $\pi$ is a distribution over actions given states

  

$$

\pi(a|s) = P[A_t = a | S_t = s]

$$

  

In other words: if you are in some state s, the distribution gives us the mapping of the probability of a specific action ( if i am here, which is the probability of going right? Or left? )

  

**The policy defines the behaviour of an agent**.

  

Policy property:

  

- In an MDP, the policy depends on the current state ant not on the whole history for the markov property.

- The policies are time independent , they are **stationary** ( they only depend on the state and not the time step )

  

Given an MDP $M = <S, A, P, R, \gamma>$ with policy $\pi$, we can always recover:

  

- Markov Process from it

- The state sequence $S_1 , S_2 , . . .$ is a MP

- Markov Reward Process from it

- The state and reward sequence $S_1, R_2, S_2 , . . .$ is a MRP $<S, P^\pi , R^\pi , \gamma >$

- $P^\pi_{ss'} = \sum_{a\in A} \pi(a|s) P^a_{ss'}$

- $R^\pi_{ss'} = \sum_{a\in A} \pi(a|s) R^a_{ss'}$

- We are just averaging over all the policy values.

  

### Value function

  

We define two types of value functions:

  

The **state-value** function $v_\pi(s)$ of an MDP is the expected return starting from state s and then following policy $\pi$

  

$$

v_\pi(s) = E_\pi[G_t| S_t=s]

$$

  

There is no one expectation anymore but there are different ones depending on how i behave.

  

The value function must be subscribed to a specified policy, in other words **it expresses how good is to be in particular state s if i’m following the $\pi$ policy.**

  

The **action-value** function $q_\pi(s,a)$ of an MDP is the expected return starting from state s, taking action a, and then following policy $\pi$

  

$$

q_\pi(s,a) = E_\pi[G_t | S_t=s, A_t=a]

$$

  

I**t tells how good is to take a particular action when we are in a particular state**

  

![image.png](images/bc438ac7-f38e-451e-a0ba-aac8cafb2f89.png)

  

### Bellman Expectation Equation

  

The value function can be decomposed into an immediate reward plus discounted value of successor state.

  

This approach can be used for both:

  

- State-value function

  

![image.png](images/08d1d769-fbe9-416b-9bff-9d448a65d952.png)

  

![image.png](images/image%2021.png)

  

We are averaging on the actions we might take.

  

Open circle represents state meanwhile filled circles are for actions

  

- Action-value function

  

![image.png](images/image%2022.png)

  

![image.png](images/image%2023.png)

  

We start off by taking some actions , we are considering a specific action as the root of the tree and we are averaging by the successor states.

  

We can now stitch together the two previous concepts:

  

- Bellman Expectation Equation for $v_\pi(s)$

  

![image.png](images/image%2024.png)

  

At the root of the tree we got the value function for a particular state V which tells us how good is it to be in a particular state and the way we are going to understand it is to use a two-step look ahead: we consider all the actions we might take next and how good is it to be in the successor states we can end after the action.

  

The idea behind the math is: the value function at the current time step is equal to the immediate reward plus the value function of where you end up.

  

- Bellman Expectation Equation for $q_\pi(s,a)$

  

![image.png](images/image%2025.png)

  

Starting from a particular state and action , i can consider the next state i can end and then the possible actions i can take from them. I can average everything like in the previous case.

  

**Example**: Bellman expectation equation in Student MDP

  

![image.png](images/image%2026.png)

  

We are considering only the red state, we want to verify that the value function of the third state 7.4 is correct.

  

The point is not a state: you are teleported instantly to one of the three states.

  

The value function is computed by considering:

  

- both probabilities of the two next states we can end up ( Study or Pub ) , we are assuming 50% 50%.

- If we study, we get a 10 reward ( 0.5 * 10 )

- If we go into a pub, we might go to multiple states each with a specific probability ( e.g. 0.4 that i come back to the exact same state of before )

- I multiply each probability with each value function and i sum up for all the possible states.

  

Bellman expectation equation can be expressed using the induced MRP:

  

$$

v_\pi = R^\pi + \gamma P^\pi v_\pi

$$

  

Value function can be computed directly as we have seen before

  

$$

v_\pi = (I-\gamma P^\pi)^{-1} R^\pi

$$

  

We will see other more efficient way of finding its solution.

  

### Optimal Value Function

  

In general we want to find the optimal way to solve your problem ( we want to find the best path through the system ).

  

The optimal value function is defined as:

  

- Optimal state-value function $v_*(s) = \max_\pi v_\pi(s)$

  

It is the maximum value function over all policies: we care about the best of all the policies we can follow, in other words we care about understanding what is the maximum possible amount of reward in expectation we can extract from the system.

  

![image.png](images/image%2027.png)

  

- Optimal action-value function $q_*(s,a) = \max_\pi q_\pi(s,a)$

  

It is the maximum action-value function over all policies.

  

It tells us the maximum amount of rewards you can extract in state s and taking action a, in other words: it tells us the most possible reward we can get if we are in a state s and we take an action a. It tells us immediately the right action to take: **solving an MDP means finding an $q_\star(s,a)$.**

  

![image.png](images/image%2028.png)

  

### Optimal Policy

  

The thing that we care about is the optimal policy: the best optimal way of behaving in an MDP.

  

A policy is just a stochastic mapping from states to actions that we take. We need to define a partial ordering over policies ( to define optimality we need to compare policies ):

  

$$

\pi \geq \pi' \quad \text{if} \quad v_\pi(s) \geq v_{\pi'}(s), \forall s

$$

  

One policy is better than another policy if the value function for that policy is greater than the value function of the other one in all the states. It means that if for one state, the value function is worse than the other , the policy is not greater or equal.

  

![image.png](images/image%2029.png)

  

We can find the optimal policy by maximizing over $q_\star(s,a)$

  

![image.png](images/image%2030.png)

  

We pick the action that gives us the most $q_\star(s,a)$: in a state s we just pick the action a with probability 1 if taking that action will give us the maximum possible reward.

  

There is always a deterministic optimal policy for any MDP.

  

If we know $q_\star(s,a)$ , we immediately have the optimal policy.

  

**Example:** optimal policy for student MDP

  

![image.png](images/image%2031.png)

  

We take the action , for each state, that maximizes $q_\star$ : e.g. in the third state ( last one on the right ) we choose to go to study because the $q_\star = 10$ and going to a pub is $q_\star = 8.4$.

  

### Bellman Optimality Equation

  

- Bellman Optimality Equation for $v_\star$

  

![image.png](images/image%2032.png)

  

Look at the action you can take and pick the max of them ( we are not averaging as before )

  

- Bellman Optimality Equation for $q_\star$

  

![image.png](images/image%2033.png)

  

In this case we don’t know what the environment / dynamic might do to us : it is like going to the Pub and we don’t know what it happens and where we will end up. Each of those states that we end up in has some optimal value and we just average them.

  

We don’t take the maximum because we don’t know where the wind will blow us, we can just average it.

  

We can now put these two pieces together and we have:

  

- Bellman optimality equation for $v_\star$

  

![image.png](images/image%2034.png)

  

Max operation is applied to all the equation.

  

we have a recursive relationship that relates $v_\star$ to itself.

  

It is two step look ahead: we are looking ahead over the actions we can take here and maximizing over those and we are also looking ahead over the dice that the environment might roll ( we don’t control the dice so we can not maximizing it instead we average over the dice that the environment can roll ).

  

- Bellman optimality equation for $q_\star$

  

![image.png](images/image%2035.png)

  

We can do the same think but for q, getting a recursive relationship. We average over the dice , so wherever the wind gets us we have to take an action and we will take the one that maximizes the $q_\star$.

  

**Example**: Bellman optimality equation in student MDP

  

![image.png](images/image%2036.png)

  

Here we are not considering any noise: if we take that action (e.g. Facebook ) we are always ending in a specific state ( e.g. upon ). In this example we are computing the $v_\star(s)$ for the red state: we are taking the maximum values between the two $v_\star$ that we have after taking two different actions.

  

### Solving the Bellman Optimality Equation

  

Bellman optimality equation is non linear ( the max operation is fundamentally nonlinear ) and in general it has not a closed form solution therefore we need iterative solution methods:

  

- Value iteration

- Policy iteration

- Q-learning

- Sarsa

  

# Planning by Dynamic Programming

  

Dynamic programming is a method for solving complex problems by breaking them down into subproblems: we solve subproblems and then we combine their solutions.

  

Dynamic programming is a general solution method for problems which have two properties:

  

- Optimal substructure → optimal solution can be decomposed into subproblems

- Overlapping subproblems → solutions can be cached and reused because subproblems recur many time

  

MDPs satisfy both properties:

  

1. Bellman equation are recursive

2. Value function stores and reuses solutions

  

Dynamic Programming assumes full knowledge of the MDP therefore it is used for *planning problems* where the environment is known ( we have a model for it ).

  

We can solve two special cases of planning an MDP

  

1. Prediction problem, given as input an MDP $<S, A, P, R, \gamma >$ and a policy $\pi$ , the output will be the value function $v_\pi$

2. Control problem, given as input an MDP $< S, A, P, R ,\gamma >$ we get as output both optimal value function $v_\star$ and optimal policy $\pi_\star$

  

## Policy Evaluation

  

We want to evaluate a given policy $\pi$ by an iterative application of Bellman expectation backup.

  

We will start with an arbitrary initial value function $v_1$ ( it can be seen as a vector of all 0 ) , we apply one iteration of the bellman expectation to get $v_2$ and so on for many times and at then we end up with the true value function $v_\pi$ ( the convergence will be discussed later ).

  

We will do it by using synchronous backups:

  

- At each iteration k+1

- We consider all the states $s \in S$

- Synchronous because we are considering all the states at any step

- Update the value function $v_{k+1}(s)$ from $v_k(s')$ where s’ is the successor state of s

  

The value function of the next iteration can be defined as:

  

![image.png](images/image%2037.png)

  

$$

v_{k+1}(s) = \sum_{a \in A} \pi(a|s) \left( R_s^a + \gamma \sum_{s' \in S} P_{ss'}^a v_k(s') \right)

$$

  

**Example**: Evaluating a random policy in the small gridworld

  

![image.png](images/image%2038.png)

  

A 4x4 grid where the shaded states are the terminal states ( if you end up in this state , no more reward, you get blocked there, end of the episode ).

  

In each state we have 4 actions ( right, left, up and down ) , we get a reward of -1 per step regardless of which action we take: we want to understand how long it takes you to reach one of these gray state where the reward is 0 ( how many steps? ) .

  

It is an undiscounted episodic MDP ( $\gamma =1$ ).

  

We can consider the simplest policy we can think of which is uniform random: each action has 1/4 probability of being chosen.

  

$$

\pi(n|\cdot) = \pi(e|\cdot) = \pi(s|\cdot) = \pi(w|\cdot) = \frac{1}{4} = 0.25

$$

  

![image.png](images/image%2039.png)

  

![image.png](images/image%2040.png)

  

The initial estimate is just 0 everywhere.

  

Any value function can be used to compute a better value function.

  

## Policy Iteration

  

We want to make our policy better, how can we do that?

  

Given a policy $\pi$:

  

1. We **evaluate** the policy

  

$$

v_\pi(s) = E[R_{t+1} + \gamma R_{t+2} + ... | S_t = s]

$$

  

1. We **improve** the policy by acting greedy wrt $v_\pi$ ( as we did in the right column of the last example )

  

$$

\pi' = \text{greedy}(v_\pi)

$$

  

In general, this process needs more iteration of improvement/evaluation but this process of **policy iteration** always converges to $\pi_*$

  

![image.png](images/image%2041.png)

  

We start from some inputs as V ( all 0 ) and $\pi$ ( a policy ): we have a cycle of evaluation and improvement where first we compute the value function according to the current policy and then we update the policy taking into account the value function.

  

In the graph going up means policy evaluation ( by iterative approach ) and going down means policy improvement ( by acting greedy ).

  

We are going now to express this idea in a more formal way:

  

1. We start off with some deterministic policy $a = \pi(s)$

2. We improve our policy by acting greedily

  

$$

\pi'(s) = \argmax_{a\in A} q_\pi(s,a)

$$

  

1. Acting greedily improves the value from any state s over just one step

  

$$

q_\pi(s,\pi'(s)) = \max_{a \in A} q_\pi(s,a) \geq q_\pi(s,\pi(s)) = v_\pi(s)

$$

  

It says that the action-value function following the $\pi$ policy but applying the $\pi'$ only for the next step for choosing the action it is always greater or equal to the action-value function following the $\pi$ policy and applying also $\pi$ to the next step.

  

It is a mathematical way of saying: the value function improves over one step at least.

  

1. We can iterate this approach using a telescoping argument

  

![image.png](images/image%2042.png)

  

The first line says that taking our greedy policy for one step is better than the thing we started with.

  

We unroll this definition to show that this is true for multiple step: it is better for two steps, for three and so on ).

  

1. If the improvements stop then the bellman optimality equation has been satisfied.

  

$$

q_\pi(s,\pi'(s)) = \max_{a\in A} q_\pi(s,a) = q_\pi(s,\pi(s)) = v_\pi(s)

$$

  

Therefore $v_\pi(s) = v_\star(s) \quad \forall s\in S$ and $\pi$ is an optimal policy.

  

### Modified Policy Iteration

  

The basic idea is to stop early, we don’t necessarily need to converge to $v_\pi$:

  

- We can introduce a stopping condition ( e.g. $\epsilon$-convergence of value function )

- We can stop after k iterations of iterative policy evaluation

  

## Value Iteration Algorithm

  

An optimal policy $\pi_*$ in current state $s$ consists of two parts:

  

1. Choose the best action $A_*$ in the current state $s$

2. Then, from the next state $s'$, follow the optimal policy $\pi_*$

  

Therefore, if $\pi_*$ is optimal globally, then $\pi_*$ must also be optimal *locally* from any state you reach.

  

![image.png](images/image%2043.png)

  

In other words, a policy is optimal starting from state s if and only if : for every successor state s' you can reach from s , the policy π is also optimal from that successor state s'.

  

> **Your policy is optimal if and only if it keeps being optimal everywhere you go**
  
We are going to use this to build **value iteration algorithm:** we can think of this as like a backward induction algorithm , the value function is caching our solutions to all of our subproblems.

  

We start with final reward ( end of our problem ) and work backwards ( figuring out the optimal path ):

  

- Assuming we know the solution to subproblems $v_\pi(s')$ → we know the value functions of the next step

- The solution $v_\star(s)$ can be found by **one-step lookahead** using the bellman optimality equation.

  

$$

v_\star(s) = \max_{a\in A} R_s^a + \sum_{s' \in S} P^a_{ss'} v_\star(s')

$$

  

we apply this update iteratively.

  

**Example:** Shortest path

  

![image.png](images/image%2044.png)

  

Very similar to the past example but here we have only one terminal step and we want to find the optimal/shortest path to reach it.

  

We start by putting 0 in the final state and then go back: put -1 to the closest states and then -2 and so on.

  

Working with synchronous dynamic programming , we don’t know in advance where the goal is and for this reason we need to update every single state.

  

Summary: of value function algorithm

  

![image.png](images/image%2045.png)

  

- We use an iterative application of Bellman optimality backup to find an optimal policy ( $v_1 \rightarrow v_2 \rightarrow ... \rightarrow v_\star$ )

- We use synchronous backups

- At each iteration k+1 and for all the states $s \in S$ we update $v_{k+1}(s)$ using $v_k(s')$

- Unlike policy iteration, there is no explicit policy

- We are working directly on the value function space

- Intermediate value functions may not correspond to any policy

- At the end we will get the value function of the optimal policy

  

### Summary of Synchronous Dynamic Programming Algorithm

  

We have different types of problems:

  

![image.png](images/image%2046.png)

  

These algorithms are based on the state-value function $v_\pi(s)$ / $v_\star(s)$ and their complexity is $O(mn^2)$ per iteration with m actions and n states.

  

We can also apply them to action-value function $q_\pi(s,a)$ / $q_\star(s,a)$ and the complexity becomes $O(m^2 n^2)$ per iteration.

  

## Extensions to DP

  

### Asynchronous DP

  

DP methods described so far used *synchronous backup* ( we look at / update every single state ). *Asynchronous DP* backs up states individually , in any order ( we just pick any state we want to be the root of our backup and then we back up for that state and then we can move on immediately without having to wait until you have updated every single state ).

  

As long as we continue to select all states ( the order does not matter ) then our algorithm will still converge to optimal value.

  

The main idea is to reduce the computation.

  

We will consider three simple asynchronous DP methods:

  

- In-place DP → it is a much more a programming trick to implement DP.

  

In synchronous DP we need to store two copies of value function ( one related to the new updated values and one for the oldest values, the leaf of the tree ).

  

![image.png](images/image%2047.png)

  

In this version of DP, we just store one copy of value function

  

![image.png](images/image%2048.png)

  

- Prioritized sweeping → it keeps a priority queue that allows us to understand which states are better than others to be updated.

  

We can use the magnitude of Bellman error to guide state selection

  

$$

\left| \max_{a \in A} \left( R_s^a + \gamma \sum_{s' \in S} P^a_{ss'} v(s') \right) - v(s) \right|

$$

  

The magnitude of error between what we thought before and what we think after can guide our selection of which states to updated.

  

We backup the state with the largest remaininig Bellman error ( it requires the predecessor states ).

  

- Real-time DP → we update only states that are relevant to agent.

  

We run an agent in the real world and we collect real samples and we update around those real samples.

  

![image.png](images/image%2049.png)

  

We use real experience of the agent as a guide to seed the dynamic programming helping it find interesting states to update.

  

### Full-Width and Sample Backups

  

Dynamic programming uses full width backup: means that for each backup every successor state and action is considered in the tree ( This requires knowing the complete MDP model ).

  

![image.png](images/image%2050.png)

  

DP is effective for medium-sized problems ( milions of states ) but for large problems it suffers Bellman’s curse of dimensionality ( the number of states grow exponentially ) and even one backup can be too expensive.

  

**Sample backups**

  

Instead of using the full probability distributions (reward function $R$ and transition dynamics $P$), you use ****actual samples ****from real experience as tuples of (S, A, R, S'). Update using just ONE sampled transition. You only need one experience tuple, not the full distribution

  

> instead of someone telling us the dynamic we just from them and see what happens.

>

- S is the current state

- A is the action taken

- R is the reward received

- S’ is the next state

  

Advantages:

  

- Model-free → there is no need of advance knowledge of MDP

- The curse of dimensionality is solved through sampling

- Cost of backup becomes constant , independent of $n=|S|$

  

This is the conceptual bridge from planning algorithms (which assume you know the MDP) to learning algorithms (which learn from experience). In RL, you don't have R and P—you collect samples and learn from them.

  

# Model-free Prediction

  

We want to estimate the value function of an unknown MDP given a specific policy ( in the previous case we saw how to resolve a *known* MDP ).

  

## Monte-Carlo Learning

  

MC methods learn directly from complete episodes of experience ( it is very suitable for episodic tasks e.g. a game where we start and we play for some number of steps and then the episode always terminates ). It uses the simples idea: the value function of a specific state is the mean return from the samples.

  

MC is model free ( it does not require knowledge of MDP transitions/rewards ) but it can be applied only to **episodic** MDPs ( all episodes must terminated ).

  

We want to use **Monte-Carlo approach for the policy evaluation**: the goal is to learn the value-function $v_\pi$ from episodes of experience under the policy $\pi$

  

$$

S_1 , A_1, R_2, . . . , S_k \sim \pi

$$

  

Recalls:

  

- **Return** is the total discounted reward

  

$$

G_t = R_{t+1} + \gamma R_{t+2} + . . . + \gamma^{T-1} R_T

$$

  

- **Value function** is the expected return

  

$$

v_\pi(s) = E_\pi\left[ G_t | S_t = s \right]

$$

  

Monte carlo policy evaluation uses **empirical mean** return instead of expected return.

  

### First-Visit Monte-Carlo Policy Evaluation

  

To evaluate a state $s$ we consider the very first time-step $t$ that we visit it in an episode.

  

We want to average over multipli episodes when i visit for the first time the state:

  

- We increment the counter that expresses how many times we visited that state over all the episodes

  

$$

N(s) \leftarrow N(s)+1

$$

  

- We increment total return

  

$$

S(s) \leftarrow S(s) + G_t

$$

  

Now i could just get the mean return from that state onwards

  

$$

V(s) = \frac{S(s)}{N(s)}

$$

  

By the law of large numbers:

  

$$

V(s) \rightarrow v_\pi(s) \quad \text{as} \quad N(s) \rightarrow \infty

$$

  

### Every-Visit Monte-Carlo Policy Evaluation

  

It is the same as before but we are evaluating a single state s by considering not only the first visit in that episode but every visit to that state.

  

**Every time-step** t a state is visited in a specific episode:

  

- Increment the counter

  

$$

N(s) \leftarrow N(s) +1

$$

  

- Increment total return

  

$$

S(s) \leftarrow S(s) + G_t

$$

  

And the value function is estimated as the mean return

  

$$

V(s) = \frac{S(s)}{N(s)}

$$

  

And by the law of large numbers

  

$$

V(s) \rightarrow v_\pi(s) \quad \text{as} \quad N(s) \rightarrow \infty

$$

  

**BlackJack Example**:

  

![image.png](images/image%2051.png)

  

We have three state variables:

  

- Current sum ( between 12 and 21 )

- The card of the Dealer which is immediately visible ( ace-10 )

- Usable ace ( yes-no )

  

We apply monte carlo evaluation policy to this problem by considering a very basic policy: we stick if sum of cards is $\geq 20$ otherwise we twist.

  

![image.png](images/image%2052.png)

  

The height of these points tell use the probability of winning the game ( the value function in other words )

  

we roll out 10,000 and 500,000 episodes of blackjack.

  

We figure out the value function directly from experience: no one told us how the game works.

  

We need to compute the mean but it can also be computed incrementally avoiding to sum everything and then to divide.

  

The **incremental mean** is:

  

![image.png](images/image%2053.png)

  

The new mean is the old one plus an increment which is defined as the difference between new element and what we thought it was the mean scaled by the k factor ( we increment the mean in the direction of the error ).

  

We can now implement the **Incremental Monte-Carlo Updates:** we update $V(s)$ incrementally after each episode.

  

For each state $S_t$ with return $G_t$

  

![image.png](images/image%2054.png)

  

Sometimes we want to track a **running mean** : we want to forget old episodies ( in non stationary problem where things change a lot and we don’t want to remember everything ). To implement that we just use a constant factor $\alpha$ replacing the counter $1/N(S_t)$: we don’t correct the mean to the real value but closer.

  

## Temporal-Difference Learning

  

TD methods learn directly from episode of experience ( as before , TD methods learn from experience generated by interaction with the environment ) and it is model-free : no knowledge of MDP transitions/rewards is needed.

  

The biggest difference with MC methods is that it learns from **incomplete episodes** : we don’t need to go through all the path / to hit the wall to learn, we can also estimate the future remaining return $G_t$ ì using current value estimates:

  

- the final part of the path can be estimated

- this process of estimating a part of the path is called **bootstrapping**

- MC just uses complete episodes to get the actual return $G_t$

  

So the Simplest temporal-difference learning algorithm $T(0)$ is defined as:

  

- We update the value $V(S_t)$ toward estimated return ( not the actual one as in MC ) $R_{t+1} + \gamma V(S_{t+1})$

  

$$

V(S_t) \leftarrow V(S_t) + \alpha(R_{t+1} + \gamma V(S_{t+1}) - V(S_t))

$$

  

The estimated return is just the Bellman equation that we saw: the immediate reward and the value function of the next state.

  

- $R_{t+1} + \gamma V(S_{t+1})$ is called **TD target**

- $\delta_t =R_{t+1} + \gamma V(S_{t+1}) - V(S_t)$ is called **TD error**

  

**Example**: Driving Home

  

![image.png](images/image%2055.png)

  

The first column tells us the elapsed time, the second one is the predicted time that i need to spend to arrive home and the predicted total time is the sum of the first two columns.

  

The second row ( reach car, raining ) is an example where i saw that it is raining and i will need to go slower with my car: i need to adjust/increase the predicted time to go as consequence.

  

**Example:** Driving home with MC vs TD

  

![image.png](images/image%2056.png)

  

While the return $G_t = R_{t+1} + \gamma R_{t+2} + . .. + \gamma^{T-1} R_T$ and true TD target $R_{t+1} + \gamma v_\pi(S_{t+1})$ are unbiased estimates of $v_\pi(S_t)$ , TD uses a biased estimate of $v_\pi(S_t)$ which is

  

$$

R_{t+1} + \gamma V(S_{t+1})

$$

  

TD target **depends only on one random** action, transition , reward while the return depends on many of them: TD target has a lower variance than the return.

  

**Example:** Random Walk

  

![image.png](images/cb651197-7f1b-42bc-8af9-d6020fa7ac80.png)

  

There are two actions ( left and right ) and we are considering an uniform random policy ( 50% left, 50% right ).

  

The question is: what is the value function for this thing?

  

![image.png](images/3423f845-58be-4943-931a-eed7b9bd21d5.png)

  

This is TD algorithm ( in particular TD(0) ).

  

We can start by initializing everything to 0.5 ( the line corresponding to 0 ) and then if we run for 1/10/100 episodes we see how the estimated values become more and more similar to the true values.

  

We can study the performance of the two algorithms MC and TD for random walk:

  

![image.png](images/image%2057.png)

  

RMS is the Root Mean Squared error.

  

## Batch MD and TD

  

We know that $V(s) \rightarrow v_\pi(s)$ with MC and TD when the amount of episodes/experience is going to infinite but what happens when we stop after a finite number of episodes?

  

![image.png](images/image%2058.png)

  

We show only $K$ episodes to the system and we keep iterating on them ( we sample iteratively the episode $k \in [1, K]$ ).

  

**Example: AB**

  

We have two states A and B with no discounting and we work with 8 episodes of experience:

  

![image.png](images/image%2059.png)

  

We want to compute $V(A)$ and $V(B)$:

  

- $V(B) = \frac{6}{8} = 0.75$

- MC will see only one Reward in state A equal to 0 and it will estimate: $V(A) = 0$.

- TD will find something much more complex ( in the image we have the maximum likelihood mdp that explains the data ) for which $V(A) = 0.25 \cdot 0 + 0.75 \cdot 1 = 0.75$

  

![image.png](images/image%2060.png)

  

Using batch solutions we have that:

  

- MC converges to solution with the minimum MSE ( best fit to the observed returns )

  

![image.png](images/image%2061.png)

  

- TD(0) converges to solution of max likelihood Markov Model ( it builds implicitly the MDP structure )

- Solution to the MDP that best fits the data

  

![image.png](images/image%2062.png)

  

## MC vs TD

  

- TD can lean before knowing the final outcome , so after every step while MC must wait until end of episode.

- TD can learn without the final outcome , from incomplete sequences ( it works in continuing non terminating environments ) while MC can only learn from complete sequences ( it works in episodic terminating environments ).

- MC has high variance but zero bias ( it has good convergence properties even with function approximation and it is not very sensitive to initial value )

- TD has low variance but it has some bias ( it is more efficient than MC but it is more sensitive to initial value ).

- TD(0) will converge to $v_\pi(s)$ but now always with function approximation

- TD exploits Markov property by building implicitly this mdp structure ( more efficient in Markov environments )

- MC does not exploit Markov property ( more effective in non-Markov environments )

  

![Screenshot 2026-01-25 alle 00.31.57.png](images/Screenshot_2026-01-25_alle_00.31.57.png)

  

**Key point:** Both converge with infinity, but TD gets more "samples" per unit time because each step is a sample, not just each episode. That's why TD is faster in practice, not because it takes fewer samples.

  

## MC vs TD vs DP backups

  

Pictorial summary of where we are, we can think of these updates as backups where we start in some state and there is a look ahead tree ( a backup diagram that we saw for DP ):

  

- Monte-Carlo Backups

  

$$

V(S_t) \leftarrow V(S_t) + \alpha(G_t - V(S_t))

$$

  

![image.png](images/image%2063.png)

  

It samples a complete trajectory/episode just by interacting with the environment.

  

- Temporal Difference Backups

  

$$

V(S_t) \leftarrow V(S_t) + \alpha \left( R_{t+1} + \gamma V(S_{t+1}) - V(S_t) \right)

$$

  

![image.png](images/image%2064.png)

  

We consider only the state ahead and we get the reward, we back up this value to update the value function the state before in the root node.

  

- Dynamic Programming Backups

  

$$

V(S_t) \leftarrow \Epsilon_\pi[R_{t+1} + \gamma V(S_{t+1})]

$$

  

![image.png](images/image%2065.png)

  

We see the state ahead but we don’t sample and for this reason we need to compute a full expectation ( we need to know the environment/dynamic, the probability of taking an action and ending in a specific state rather than another one )

  

## Bootstrapping and Sampling

  

- Bootstrapping means that we don’t actually use the real return but our estimation of it.

- Update involves an estimate

- DP and TD bootstraps while MC does not.

- Sampling means updates involving an expectation: we don’t need full width / every trajectories but just sample the mdp dynamics.

- DP does full width updates by considering every possibility exhaustively

- TD and MC sample.

  

This is the space of unified view of methods for policy evaluation

  

![image.png](images/image%2066.png)

  

## TD($\lambda$)

  

We have seen TD(0) called TD 1 step where the agent takes one action and it will end up in some successor State and we use its value function to make a prediction on the final return with its immediate return.

  

We want to generalize this concept to **n steps** and not just one.

  

![image.png](images/image%2067.png)

  

When $n=\infty$ we end up in doing Monte Carlo approach.

  

![image.png](images/image%2068.png)

  

We can generalize it by defining the **n-step return** as:

  

$$

G^{(n)}_t = R_{t+1} + \gamma R_{t+2} + . . . + \gamma^{n-1} R_{t+n} + \gamma^n V(S_{t+n})

$$

  

TD(n) is defined as:

  

$$

V(S_t) \leftarrow V(S_t) + \alpha ( G_t^{(n)} - V(S_t))

$$

  

**Example** Large Random Walk:

  

![image.png](images/image%2069.png)

  

Online means that we update immediately the value functions meanwhile Offline when we wait for the end of the episode to update them ( updates are accumulated within episode and then they are applied in batch at the end of episode ).

  

The goal is to come up with an algorithm that gets the best of all n.

  

### $\lambda-$Return

  

We want to efficiently consider all n at once , a way to do that is averaging over these N-Step Returns: we don’t have to commit to one of them, we can actually take a Target which combines multiple n-step returns together.

  

![image.png](images/image%2070.png)

  

In this case we have one back up that makes the average over the 2-step and 4-step returns. This return will be much more robust because it gets the best of both of these cases.

  

We want to do something like that but for all **n →** this is what the $\lambda-$Return algorithm does.

  

It uses the $\lambda-$return $G_t^\lambda$ which combines all n-step returns $G_t^{(n)}$ through a weighted sum.

  

### Forward-view TD($\lambda$)

  

This is the TD($\lambda$) weighting function

  

$$

G_t^\lambda = (1-\lambda) \sum_{n=1}^\infty \lambda^{n-1} G_t^{(n)}

$$

  

![image.png](images/image%2071.png)

  

![image.png](images/image%2072.png)

  

It is also called **Forward-View TD($\lambda$)** which is very similar to Monte Carlo because we have to wait all the way until the end of the episode to our n-step returns. This algorithm suffers of some of the disadvantages the we had with Monte Carlo.

  

### Backward-view TD($\lambda$)

  

We want to achieve the result of forward view but with the nice properties of TD learning where we update online, every step and using incomplete sequences.

  

$$

E_0(s) = 0\\

E_t(s) = \gamma \lambda E_{t-1}(s) + 1(S_t=s)

  

$$

  

**Eligibility traces** combine**:**

  

- Frequency heuristic: assign credit to most frequent states

- Recency heuristic: assign credit to most recent states

  

![image.png](images/image%2073.png)

  

It represent the eligibility trace for one particular state over time: we increase each time we visit a state and after a certain time that we don’ see it , the value starts to decade exponentially ( it combines both frequency and recency ).

  

Backward view TD($\lambda$) algorithm works by:

  

1. Keeping an eligibility trace for every state $s$

2. Updating value $V(s)$ for every state $s$ in proportion of TD-error $\delta_t = R_{t+1} + \gamma V(S_{t+1}) - V(S_t)$ and eligibility trace $E_t(s)$

  

$$

V(s) \leftarrow V(s) + \alpha \delta_t E_t(s)

$$

  

![image.png](images/image%2074.png)

  

## TD(0) and TD($\lambda$)

  

When $\lambda=0$ , only the current state is updated and it is equivalent to TD(0) update:

  

$$

E_t(s) = 1(S_t = s) \\

V(s) \leftarrow V(s) + \alpha \delta_t E_t(s)

$$

  

$\lambda$ says how fastly we decay this thing, if it is 0 we decay it completely straight down.

  

When $\lambda=1$ ( the other extreme ), the credit is deferred all the way to the end of the episode. Considering offline updates and an episodic environments , the total update for TD(1) is the same as total update for MC.

  

![image.png](images/image%2075.png)

  

The notation **1(S = s₁)** is an **indicator function** (also called a **characteristic function**).

  

**It means:**

  

- 1(S = s₁) = **1** if S equals s₁ (the condition is true)

- 1(S = s₁) = **0** if S does not equal s₁ (the condition is false)

  

## Summary of Forward and Backward TD($\lambda$ )

  

![image.png](images/image%2076.png)

  

# Model Free Control

  

We want to optimise the value function of an **unknown MDP →** find the most optimal behavior ( the one that extracts the most reward ).

  

For most of the following problems ( in the image ) we can model them as MDPs

  

![image.png](images/image%2077.png)

  

And the MDP model could be:

  

- Unknown, but experience can be samples

- Known but it is too big to use

  

In both cases we should relay on Model-free control approaches.

  

It is important to define:

  

- On-policy Learning → learn on the job

  

Learn about policy $\pi$ from experience sampled from $\pi$ ( we just follow the policy and we learn about it )

  

- Off-policy Learning → look over someone’s shoulder

  

Learn about policy $\pi$ from experience sampled from $\mu$ ( we are watching some other agent and we are trying to figure out the optimal behavior through it ).

  

We learn from one policy while following another

  

## On-Policy Monte-Carlo Control

  

### Generalised Policy Iteration GPI

  

GPI is the general framework of alternating evaluation + improvement:

  

![image.png](images/image%2078.png)

  

it is a loop where first we evaluate the policy ( we estimate $v_\pi$ applying an iterative policy evaluation ) and then we improve it through a greedy approach ( we generate a new policy which is always better or equal to the oldest one $\pi' \geq \pi$ ).

  

### Generalised Policy Iteration with MC Evaluation

  

The policy evaluation is estimated using MC policy evaluation $V = v_\pi$ and for the policy improvement we use greedy policy improvement.

  

However there is a big problem here:

  

- The greedy policy improvement over $V(s)$ requires a model of MDP

  

$$

\pi'(s) = \argmax_{a \in A} R^a_s + P_{ss'}^a V(s')

$$

  

When we work with the value function we need always a model to do our policy improvement ( we need to know the probability transition matrix $P_{ss'}^a$ which is related to the dynamic of the world ).

  

The **alternative** is to use $Q(s,a)$ the action-value function which enables us to do control in a model free setting.

  

$$

\pi'(s) = \argmax_{a \in A} Q(s,a)

$$

  

We will perform **Generalised Policy Iteration with Action-Value Function**

  

![image.png](images/image%2079.png)

  

**Example** Greedy Action Selection:

  

We have two doors and we are trying to pick the best door ( **bandit problem** )

  

![image.png](images/image%2080.png)

  

We are trying to resolve it using a trial and error approach.

  

Acting greedily means we always open the right door in this example forever , the problem is we don’t know what there is behind the left door: we opened it just one time.

  

In order to guarantee that we visit all states and actions we apply the $\epsilon-$Greedy Exploration: the simplest idea is either we take the best actions or we exploit it randomly:

  

- Choose the greedy action with probability $1-\epsilon$

- Choose a random action with probability $\epsilon$

  

![image.png](images/image%2081.png)

  

It ensures a continual exploration ( all m actions are tried with non-zero probability ).

  

We can define the $\epsilon-$**Greedy Policy Improvement** and its theorem as:

  

![image.png](images/image%2082.png)

  

Proof:

  

![image.png](images/image%2083.png)

  

We end up with Monte-Carlo Policy Iteration:

  

![image.png](images/image%2084.png)

  

We changed both policy evaluation ( monte carlo approach ) and improvement ( we use the $\epsilon-$greedy algorithm ).

  

It is not always necessary to fully evaluate our policy and to go to the top of this line every time;sometimes we can just spend few steps to evaluate our policy and we have already got enough information there to guide us to a much better policy without wasting many many more iterations.

  

![image.png](images/image%2085.png)

  

In the context of MC we can think of doing that in every single episode: we make our agent do one episode, collect all the steps along and we update the q-values just for those steps ( we are updating the mean value just of those visited states and tried actions along the episode ) - why wait to get more information from new episodes when we can already improve the policy?

  

![Screenshot 2026-01-23 alle 18.05.39.png](images/Screenshot_2026-01-23_alle_18.05.39.png)

  

We come up with **GLIE ( Greedy in the Limit with Infinite Exploration )** which is an algorithm used to balance exploration and acting greedily ( exploitation ).

  

It ensures the convergence of our algorithm to find $\pi^*$ and it is composed by two parts:

  

1. Infinite **exploration**→ All state-action pairs must be visited infinitely often during learning

  

$$

\lim_{k \rightarrow \infty}N_k(s,a) = \infty

$$

  

Explore widely ( high $\epsilon$ )

  

Visit every pair $(s,a)$ many times.

  

1. Greedy in the limit → eventually, the policy becomes greedy (purely **exploits**)

  

$$

\lim_{k\rightarrow\infty} \pi_k(a|s) = 1(a=\argmax_{a'\in A} Q_k(s,a'))

$$

  

As the time goes on $\epsilon$ decreases ( $\epsilon \rightarrow 0$ as $t \rightarrow \infty$ ) and we eventually stop exploring and act optimally.

  

### GLIE Monte-Carlo Control

  

The algorithm is the following one:

  

- We sample the k-th episode using $\pi$

  

$$

{S_1,A_1,R_2, ... ,S_T} \sim \pi

$$

  

- For each state $S_t$ and action $A_t$ we update our action value and we do that by increment the count and updating the mean.

  

$$

N(S_t, A_t) \leftarrow N(S_t, A_t)+1 \\

Q(S_t,A_t) \leftarrow Q(S_t, A_t) + \frac{1}{N(S_t,A_t)}\left( G_t - Q(S_t,A_t) \right)

$$

  

- After the policy evaluation steps we now want to improve our policy using the new action-value function computed

- We set $\pi$ acting greedily w.r.t. these new Q values.

- We set $\epsilon$ using the **Robbins-Monro** technique

  

$$

\epsilon \leftarrow \frac{1}{k}\\

\pi \leftarrow \epsilon-\text{greedy(Q)}

$$

  

GLIE Monte Carlo Control converges to optimal action-value function

  

$$

Q(s,a) \rightarrow q_*(s,a)

$$

  

## On-Policy Temporal Difference Learning

  

We know that TD learning has some advantages over MC:

  

- Lower variance

- Online

- It works also with incomplete sequences

  

The natural idea can be to use TD instead of MC as policy evaluation ( apply TD to $Q(S,A)$ ) and use $\epsilon-$greedy policy improvement updating every time-step.

  

The general idea is called SARSA.

  

### Updating Action-Value Functions with Sarsa

  

We start off in some state action pair (S,A), we sample from the environment in order to get the reward and what new state we end up S’ in. We are going to re-sample our policy again in order to generate A’.

  

![image.png](images/image%2086.png)

  

This is why it is called SARSA algorithm.

  

$$

Q(S,A) \leftarrow Q(S,A) + \alpha\left( R + \gamma Q(S',A') - Q(S,A) \right)

$$

  

We plug in the SARSA algorithm in our Generalization Policy Iteration framework.

  

![lecture-5-model-free-control--21.jpg](images/3387e627-8f08-4caf-9cc9-c335c755db5a.png)

  

With MC we update the action-value after each episode , with SARSA we update it after each time-step ( we don’t need to reach the episode end ).

  

It is very similar to MC but it is faster because updates happen every step, not just episode-end.

  

**Algorithm**

  

![image.png](images/image%2087.png)

  

SARSA convergese to the optimal action-value function $Q(s,a) \rightarrow q_\star(s,a)$ under the following conditions:

  

- GLIE sequence of policies $\pi_t(a|s)$

- Robbins-Monro seuqnce of step-sizes $\alpha_t$ , which means that we need to choose a step sizes $\alpha_t$ that satisfy $\sum_{t=1}^\infty \alpha_t = \infty$ and $\sum_{t=1}^\infty \alpha_t^2 < \infty$

  

**Example** Windy Gridworld

  

![image.png](images/image%2088.png)

  

We want to move from the Start point to the Goal/Target point but there is the wind that moves up the agent of a specific number of cells specified below the grid ( 0 0 0 1 … ).

  

![image.png](images/image%2089.png)

  

It shows the best optimal path and the learning curve for running Sarsa: how many timesteps are required by each episode to be completed.

  

### n-Step Sarsa

  

We consider the middle area of the spectrum that we saw before for finding a solution that takes both the advantages of MC and Sarsa.

  

We can consider the following n-step returns for $n=1,2, . . . , \infty$

  

![image.png](images/image%2090.png)

  

We can define the n-step Q return:

  

$$

q_t^{(n)} = R_{t+1} + \gamma R_{t+2} + ... + \gamma^{n-1} R_{t+n} + \gamma^n Q(S_{t+n})

$$

  

The n-step Sarsa updates become:

  

$$

Q(s,a) \leftarrow Q(s,a) + \alpha \left( q_t^{(n)} - Q(S_t,A_t) \right)

$$

  

Now we want to make the lambda version of this algorithm: we are going to average over all of our n-step returns by weighting each n-step return by a factor of $(1-\lambda) \lambda^{n-1}$

  

The $\lambda$ step return is computed as the weighted average of each n-step return:

  

$$

q_t^\lambda = (1-\lambda) \sum_{n=1}^\infty \lambda^{n-1} q_t^{(n)}

$$

  

And the **Forward-view SARSA($\lambda$)** is defined as:

  

$$

Q(S_t,A_t) \leftarrow Q(S_t,A_t) + \alpha (q_t^\lambda - Q(S_t,A_t))

$$

  

The problem with it is that we need to wait until the end of the episode to update the action-value: it is not an online update/algorithm, we don’t want to wait untill the end of the episode. For this reason we use **eligibility traces** , SARSA($\lambda$) has one eligibility trace for each state-action pair:

  

![image.png](images/image%2091.png)

  

It says how much a state and an action is responsible for getting the final return: how much that state helps to getting to the final spot.

  

$Q(s,a)$ is updated for every state and action in proportion to TD-error $\delta_t$ and eligibility trace $E_t(s,a)$:

  

$$

\delta_t = R_{t+1} + \gamma Q(S_{t+1} , A_{t+1}) - Q(S_t,A_t)

\\

Q(s,a) \leftarrow Q(s,a) + \alpha\delta_tE_t(s,a)

$$

  

This is the **Backward View Sarsa($\lambda$)**.

  

**Sarsa($\lambda$) Algorithm**

  

![image.png](images/image%2092.png)

  

**Example** Sarsa$(\lambda)$ applied to GridWorld:

  

![image.png](images/image%2093.png)

  

You propagate the importance of each step backwards and you need a lot of episodes to arrive to the initial step ( the arrow dimension represents its eligibility trace for that state and action ).

  

## Off-Policy Learning

  

While we are following a behaviour policy $\mu(a|s)$ we want to evaluate a target policy $\pi(a|s)$ to compute $v_\pi(s)$ or $q_\pi(s,a)$.

  

Reasons behind that:

  

- We want to learn from observing humans or other agents

- We want to re-use experience generated from old policies.

- We want to learn about optimal policy while following exploratory policy

- We want to learn about multiple policies while following one policy

  

### Importance Sampling

  

It is the first off policy learning mechanism: we estimate the expectation of a different distribution

  

![image.png](images/image%2094.png)

  

We take this expectation and we say that an expectation over our future reward is just sum over some probabilities times how much reward we got. We multiply and divide by a new Distribution and it becomes an expectation over the new distribution of something else that just $f(X)$.

  

![Screenshot 2026-01-24 alle 19.06.44.png](images/Screenshot_2026-01-24_alle_19.06.44.png)

  

This is the foundation of off-policy learning:

  

- You can learn about an optimal policy P

- While following an exploratory policy Q

- By weighting samples appropriately

  

**1. Importance Sampling for Off-Policy Monte-Carlo**

  

We use the returns generated from $\mu$ to evaluate $\pi$ and we weight the return $G_t$ according to similarity between policies.

  

We have to multiply these important sampling rations across all the entire trajectory like every single step ( the it does not work because over many steps our target policy and behaviour policy never match enough for it to be useful ).

  

![image.png](images/image%2095.png)

  

We multiply these ratios for every step in the entire trajectory (from t to T), each ratio is composed by two small numbers ( two probabilites ) which will give us a big number if the two policies are not aligned / different ( e.g. $\frac{0.9}{0,1} = 9$ ).

  

For some trajectories the two policies diverge and the weights become astronomically large ( trajectories with a lot of steps can end with weights in terms of $10^{10}$ ).

  

We update value towards corrected return

  

$$

V(S_t) \leftarrow V(S_t) + \alpha(G_t^{\pi/\mu} - V(S_t))

$$

  

It is extremely high variance and in practice **it is just useless.**

  

**2. Importance Sampling for Off-Policy TD**

  

When we work with off policy learning we need to use TD ( MC is unavailable due the high variance ).

  

We apply importance sampling not to whole trajectory but just for one single step: we just use one importance weight $\frac{\pi(A_t|S_t)}{\mu(A_t|S_t)}$ giving us a much more stable update

  

$$

G_t^{\pi/\mu} = \frac{\pi(A_t|S_t)}{\mu(A_t|S_t)} G_t

$$

  

Where $G_t = R_{t+1} + \gamma V(S_{t+1})$

  

We get our final update rule:

$$

V(S_t) \leftarrow V(S_t) + \alpha \left( \frac{\pi(A_t|S_t)}{\mu(A_t|S_t)} (R_{t+1} + \gamma V(S_{t+1})) - V(S_t) \right)

$$

It has much lower variance than MC importance sampling because policies need to be aligned/similar only over a single step.
### Q-Learning
We now consider off-policy learning of action-values $Q(s,a)$ and no importance sampling is required.
We are going to select our next action using our behaviour policy $\mu$ but we are going to consider also some alternative successor action that we might have taken following our target policy $\pi$.

How it works:
- Take action from behavior policy $A_t \sim \mu(\cdot |S_t)$ → we follow an exploratory policy
- Consider an alternative action $A' \sim \mu(\cdot | S_t)$ instead of using the action you actually took → we imagine what the target policy would do
- Update $Q(S_t, A_t)$ towards that alternative action→ we bootstrap from the alternative action’s value.
$$
Q(S_t, A_t) \leftarrow Q(S_t,A_t) + \alpha \left( R_{t+1} + \gamma Q(S_{t+1}, A') - Q(S_t, A_t) \right)
$$

The importance weight is built into the action selection and there is no nedd for importance sampling corrections ( no need for an explicit weight and for this reason we are avoiding the variance problem ).
The weighting is not needed because we are not directly computing an expectation under $\pi$ but we are using the **max operator**

$$

\pi(S_{t+1}) = \argmax_{a'} Q(S_{t+1},a')

$$

The target policy $\pi$ is **greedy** w.r.t. $Q(s,a)$ and the behaviour policy is acting $\epsilon-$greedy ( exploitation and exploration ) :both of them are improving!

Key insight: The max is not a sample from any policy!

  

- You don't sample A' from π

- You don't sample A' from μ

- You deterministically pick the best action using argmax

- This implicitly represents the optimal policy

  

Q-learning target simplifies to:

  

![image.png](images/image%2096.png)

  

**Q-Learning Control algorithm** ( with SARSAMAX updateds ):

  

![image.png](images/image%2097.png)

  

Q learning updates a little bit in the direction of the best/maximum Q value that you could have after one step.

  

![image.png](images/image%2098.png)

  

Theorem: Q-Learning algorithm control converges to the optimal action-value function $Q(s,a) \rightarrow q_\star(s,a)$.

  

### Relationship between DP and TD

  

![lecture-5-model-free-control--41.jpg](images/71c950f8-e889-4ed8-bb86-19d17f01b351.png)

  

![image.png](images/image%2099.png)

  

In general, for Bellman Expectation Equation we can use DP or we can just sample it using TD. We can think of TD as a sampling of the bellman expectation/optimality equations.

  

**TD algorithms are sampled versions of the corresponding DP algorithms.**

  

![Screenshot 2026-01-25 alle 00.26.53.png](images/Screenshot_2026-01-25_alle_00.26.53.png)

  

![Screenshot 2026-01-25 alle 00.30.23.png](images/Screenshot_2026-01-25_alle_00.30.23.png)

  

The environment naturally samples according to $P(s'|s,a)$ because we will sample n times and it is normal that we will get more values that are much more probable which will move the average towards them implicitly.

  

This table shows that **every DP algorithm has a TD counterpart**. You don't need to memorize separate algorithms—understand the Bellman equations and whether you're doing full backups or sampling.

# Value Function Approximation

  

RL can be used to solve large problems ( with a lot of number of states ) like:

  

- Backgammon: $10^{20}$

- Computer Go: $10^{170}$ states

- Helicopter: continuous state space

  

When we work with continuous state space, we can not build a table where we have a separate value for each state because it is not going to scale up. We need model-free methods that scale up for prediction and control: we need a value function approximation.

  

So far we have represented the value function as a **lookup table** where every state s has an entry $V(s)$ or every state s and action s pair has $Q(s,a)$. For problem with large MDPs , there are too many states/actions to store and it is too slow to learn the value of each of them individually. We **estimate** our value function with **parametric function approximation:**

  

$$

\hat{v}(s,\textbf{w} ) \approx v_\pi(s) \\

\hat{q}(s,a,\textbf{w}) \approx q_\pi(s,a)

$$

  

$\textbf{w}$ is a vector of weights ( e.g. parameters of NN ).

  

We want to build a function approximation that fits $v_\pi(s)$ or $q_\pi(s,a)$ across the whole state space ( and action space ) using a compact representation through a smaller number of weights than the states ( and actions ) in the whole state space ( and action space ).

  

Using a small number of weights w.r.t the total number of states allows us to decrease the memory required but also to generalize from seen states to unseen ones by querying the function approximation.

  

We will do that by updating these weights/parameters using the methods seen so far ( MC or TD learning ).

  

There are three different types/architectures of function approximations :

  

1. State-value function approximation

![image.png](images2/03b5fb3b-0da9-4664-a768-0bcdb26ac03f.png)

2. Action-value function approximation → we have got two choices

3. Action in Action-value function approximation → i am in the state s and i am considering the action a, how good would that be? The function approximator will give us the estimator by using the weights

![image.png](images2/43a0a94a-4dee-41f5-960d-c1e2c0909a0f.png)

2. Action out Action-value function approximation → we want in state s and we want our function approximator to tell us the value of all actions that i might take.

![image.png](images2/image.png)

  

We can use anything we like as black box function approximator, any tool:

  

- Linear combinations of feature

- Neural Network

- Decision Tree

- Nearest Neighbour

- Fourier bases

- ecc…

  

BUT we must consider **differentiable** function approximators ( first two of this list ) and a training method that is suitable for non-stationary and non-iid data.

  

## Incremental methods

  

### Gradient Descent

  

Considering a differentiable function $J(\textbf{w})$ of parameter vector **w** , we can define its gradient as:

  

![image.png](images2/image%201.png)

  

![image.png](images2/image%202.png)

  

It gives us the direction of the steepest descent/ascent and we are going to follow this downhill in order to find a local minimum of $J(\textbf{w})$.

  

We adjust our parameters $\textbf{w}$ in the direction of the gradient ( downhill due the minus)

  

$$

\Delta \textbf{w} = - \frac{1}{2} \alpha \nabla_{\textbf{w}}J(\textbf{w})

$$

  

where $\alpha$ is a step-size parameter.

  

We want to use it in value function approximation, in this case we are assuming we are doing supervising learning: someone ( an oracle ) is giving use the true $v_\pi(s)$ .

  

We want to find a parameter vector $\textbf{w}$ minimize the Mean Squared Error ( MSE ) of the difference of the approximate value function $\hat{v}(s,\textbf{w})$ and true value function $v_\pi(s)$

  

$$

J(\textbf{w}) = E_\pi[(v_\pi(S) - \hat{v}(S,\textbf{w})^2]

$$

  

We use the gradient descent to find a local minimum ( we plug in the approximation function chosen )

  

![image.png](images2/image%203.png)

  

We apply the chain rule and we know that our oracle does not depend on $\textbf{w}$.

  

Instead of explicitly computing this expectation , we are going to randomly sample a state ( by just seeing which state we visited ) which is called **Stochastic Gradient Descent** ( which samples the gradient )

  

$$

\Delta \textbf{w} = \alpha( v_\pi(S) - \hat{v}(S,\textbf{w})) \nabla_\textbf{w} \hat{v}(S,\textbf{w})

$$

  

Even if we change things online ( updates step after step ) then we still arrive at minimizing what we want.

  

Stochastic gradient descent (SGD) does **not** guarantee convergence to the global optimum in non-convex problems. It typically converges to a local optimum or saddle point.

  

### Linear Function Approximation

  

We want represent a state by a **feature vector**

  

![image.png](images2/image%204.png)

  

Each of these features is a property ( a number ) which tells you some piece of information about our state→ Each feature is a representation that characterizes the state space.

  

Examples:

  

- Distance of robot from landmarks

- Trends in the stock market

  

Supposing someone gave us our feature vector ( how to find me will not be covered in this course ) , we can approximate the value function by a linear combination of features

  

$$

⁍

$$

  

Its objective function is the MSE which is quadratic in parameters $\textbf{w}$

  

$$

J(\textbf{w}) = E_\textbf{w}[(v_\pi(s) - x(S)^T\textbf{w})^2]

$$

  

Stochastic gradient descent converges to the global optimum due to the quadratic and convex nature of the function.

  

The update rule is particularly simple:

  

![image.png](images2/image%205.png)

  

**Table Lookup** is a special case of linear value function approximation where we use table lookup features:

  

![image.png](images2/bfdd86b4-8614-47fe-9361-e103359327d5.png)

  

That says if i am in state one i have a feature value of one otherwise i will have 0 and all way down until the final state: all of them are 0 except for the one related to state where i am now ( one hot encoding ).

  

If we use this approach, the approximation just consists of selecting one weight value.

  

![image.png](images2/bc58cc50-42b9-4083-b537-62835205fdf6.png)

  

### Incremental Prediction Algorithm
In the previous techniques we have assumed we knew the true value function $v_\pi(s)$  but in RL there is no supervisor, only rewards.
In practise we replace $v_\pi(s)$ with a *target*:
- For MC , the target is the return $G_t$
$$
\Delta w = \alpha(G_t - \hat{v}(S_{t+1},\textbf{w} )) \nabla_\textbf{w}\hat{v}(S_{t+1})
$$
- For TD(0), the target is the TD target $R_{t+1} + \gamma \hat{v}(S_{t+1},\textbf{w})$
$$
\Delta w = \alpha(R_{t+1} + \gamma \hat{v}(S_{t+1},\textbf{w}) - \hat{v}(S_{t+1},\textbf{w} )) \nabla_\textbf{w}\hat{v}(S_{t+1})
$$
- For TD($\lambda$), the target is $\lambda-$return $G_t^\lambda$
$$
\Delta w = \alpha(G_t^\lambda - \hat{v}(S_{t+1},\textbf{w} )) \nabla_\textbf{w}\hat{v}(S_{t+1})
$$
We are doing supervisor learning on the returns.

#### Monte Carlo with Value Function Approximation
We are going to use the return $G_t$ which is an unbiased , noisy sample of the true value $v_\pi(S_t)$.
We want to apply supervised learning to training data:
![[Pasted image 20260125163659.png]]
We see the state $S_1$  and we run a trajectory from it and we see that we got a return of $G_1$ , all the way up to our final state $S_T$ and its final return $G_T$.
We are treating it as dataset and we are adjusting our function approximator to fit the $G$s, the simplest case is using *linear Monte-Carlo policy evaluation*
![[Pasted image 20260125164219.png]]
Monte-Carlo evaluation converges to a local optimum even when using non-linear value function approximation.

#### TD  Learning with Value Function Approximation
We are going to use the TD target $R_{t+1} + \gamma \hat{v}(S_{t+1},\textbf{w})$ which is an unbiased , noisy sample of the true value $v_\pi(S_t)$.
We want to apply supervised learning to training data as before:
![[Pasted image 20260125165103.png]]
 The simplest case is using *TD(0)*:
 ![[Pasted image 20260125165245.png]]
 It converges close to global optimum.
#### TD($\lambda$)  Learning with Value Function Approximation
We are going to use the $\lambda-$return $G_t^\lambda$  which is a biased example of the true value $v_\pi(S_t)$.
We want to apply supervised learning to training data as before:
![[Pasted image 20260125165712.png]]
We can approximate the value function either using:
- Forward view linear TD($\lambda$)
![[Pasted image 20260125165926.png]]
- Backward view linear TD($\lambda$)
![[Pasted image 20260125165940.png]]


### Incremental Control Algorithm
![[Pasted image 20260125171213.png]]
We are going to use approximate policy evaluation: we start off with some parameter vector now which defines some value function ( could be a neural network weights or some other tools ). We act greedily with a little bit of epsilon exploration ( *$\epsilon-$greedy policy improvement*) w.r.t. our value function that we have defined ( w.r.t. $\hat{q}(\cdot, \cdot, \textbf{w})$). After that we will obtain a new policy and we want to evaluate it ( we compare the prediction versus the reality by taking samples from the environment and we update the parameters of our neural network , the weights, in the direction that reduces this error )that gives us a new value function and so far ( it is a loop that ends when $q_\textbf{w} = q_\star$)
![[Screenshot 2026-01-25 alle 17.19.09.png]]

#### Action-Value Function Approximation
We will do the same steps again using Q instead of V.
We are going to approximate the action-value function
$$
\hat{q}(S,A,\textbf{w}) \approx q_\pi(S,A)
$$
We want to minimise the MSE between approximation action value $\hat{q}(S,A,\textbf{w})$ and the true action value functions $q_\pi(S,A)$
$$
J(\textbf{w}) = E_\pi\left[(q_\pi(S,A) - \hat{q}(S,A,\textbf{w}))^2\right]
$$
We apply the stochastic gradient descent to find a local minimum
$$
- \frac{1}{2}\nabla_\textbf{w}J(\textbf{w}) = (q_\pi(S,A) - \hat{q}(S,A,\textbf{w})) \nabla_\textbf{w} \hat{q}(S,A,\textbf{w})
$$
$$
\Delta \textbf{w} = \alpha(q_\pi(S,A) - \hat{q}(S,A,\textbf{w})) \nabla_\textbf{w} \hat{q}(S,A,\textbf{w}) 
$$

#### Linear Action-Value Function Approximation
We represent a state and an action by a **feature vector**:
![[Pasted image 20260126145636.png]]
We can re-write the action-value function by linear combination of features:
![[Pasted image 20260126145814.png]]
The stochastic gradient update will be:
![[Pasted image 20260126145833.png]]
For incremental control algorithms we need to replace the target $q_\pi(S,A)$:
- Using MC, the target becomes $G_t$
$$
\Delta \textbf{w} = \alpha \left( G_t - \hat{q}(S_t,A_t,\textbf{w})\nabla_\textbf{w}\hat{q}(S_t,A_t,\textbf{w}) \right)
$$
- Using TD(0), the target becomes the TD target $R_{t+1} + \gamma Q(S_{t+1}, A_{t+1})$
$$
\Delta \textbf{w} = \alpha \left(R_{t+1} + \gamma Q(S_{t+1}, A_{t+1})  - \hat{q}(S_t,A_t,\textbf{w})\nabla_\textbf{w}\hat{q}(S_t,A_t,\textbf{w}) \right)
$$
- Using forward-view TD($\lambda$), the target becomes the action-value $\lambda$ return
$$
\Delta \textbf{w} = \alpha \left(q_t^\lambda  - \hat{q}(S_t,A_t,\textbf{w})\nabla_\textbf{w}\hat{q}(S_t,A_t,\textbf{w}) \right)
$$
- Using backward-view TD($\lambda$), the update is
$$
\delta_t = R_{t+1} + \gamma \hat{q}(S_{t+1},A_{t+1},\textbf{w}) - \hat{q}(S_{t},A_{t}
$$
$$
E_t = \gamma \lambda E_{t-1} + \nabla_\textbf{w}\hat{q}(S_t,A_t,\textbf{w})
$$
$$
\Delta \textbf{w} = \alpha \delta_t E_t
$$

**Example**: Linear Sarsa with Corse Coding in Mountain Car
![[Pasted image 20260126151347.png]]
A car is stuck in a valley and needs to reach the goal at the top. The car is underpowered—it can't climb directly. It must build momentum by oscillating back and forth.
The state space is the position of the car and its velocity ( both are continuous ).

###  Convergence of prediction algorithms 
Following Monte Carlo is just like a noisy Oracle , we are doing supervised learning so it must converge. Is that true for TD methods?
No, TD is not guaranteed to be a stable algorithm : it can blow up.
![[Pasted image 20260126153324.png]]
This is a summary of convergence of prediction algorithms.
TD methods are not the best choice for Off-policy learning.

### Gradient Temporal-Difference Learning
Bootstrapping can prevent the convergence of the algorithm. TD diverges when off-policy or using nonlinear function approximation because it does not follow the gradient of any objective function.
**Gradient TD** follows true gradient of projected Bellman error
![[Pasted image 20260126153823.png]]

### Convergence of Control Algorithms
There is no guarantee once you use function approximation that your improvement step is really improving the policy
![[Pasted image 20260126153954.png]]

# Batch Methods
The batch in this case is the agent's experience ( considered as training data ).
We have seen gradient descent but it does not sample efficiently while batch methods seek to find the best fitting value function over our batch.
![[Screenshot 2026-01-26 alle 15.45.53.png]]

## Least Square Prediction
One definition of finding the best fit is finding a least square fit.
$$
\hat{v}(s,\textbf{w}) \approx v_\pi(s) 
$$
We consider a training data set as *experience* D composed of <state,value> pairs
![[Pasted image 20260126155840.png]]
We want to find the best parameters $\textbf{w}$ that give the best fitting value function $\hat{v}(s, \textbf{w})$
Least squares algorithms find parameter vector  $\textbf{w}$ minimising sum-squared error between  $\hat{v}(s_t, \textbf{w})$ and target values $v_t^\pi$
![[Pasted image 20260126160607.png]]
We see that mathematically 
$$ MSE = \frac{1}{n} \text{Least Squares}$$
There is a very easy way to find the least square solution by using **Stochastic Gradient Descent with Experience Replay**: given an experience cached/stored
![[Pasted image 20260126155840.png]]
we repeat:
1. Sample state and a value from our experience
$$
<s,v^\pi> \sim D
$$
2. Apply SGD update towards the sampled target
$$
\Delta \textbf{w}= \alpha(v^\pi- \hat{v}(s,\textbf{w})) \nabla_\textbf{w}\hat{v}(s,\textbf{w})
$$
It is like supervising learning.
This algorithm converges to the least square solution
$$
\textbf{w}^\pi = \argmin_\textbf{w} LS(\textbf{w})
$$
### Experience Replay in Deep Q-Networks
DQN uses **experience replay** and **fixed Q-targets**:
- Take an action $a_t$ according to $\epsilon-$greedy policy w.r.t. our value function approximator
- We store the transition $(s_t,a_t,r_{t+1},s_{t+1})$ in replay memory D
- Sample random mini-batch of transitions $(s,a,r,s')$ from our replay memory D
- Compute Q-learning targets w.r.t. old, fixed parameters $\textbf{w}^-$
	- We freeze the targets in other to get more stability 
- Optimise MSE between Q-network is predicting ( our action-value function ) and our Q-learning targets 
![[Pasted image 20260127090848.png]]
- We optimize it by using stochastic gradient descent

This method is stable with neural networks due the experience replay approach ( it decorrelates the trajectories and we use two networks, one with the old parameters and one with the new parameters ).

How much does DQN help?
![[Pasted image 20260127091825.png]]

### Linear Least Squares Prediction Algorithms
It may take many iterations for experience replay to find a least squares solution. If we use a linear value function approximation $\hat{v}(s,\textbf{w}) = x(s)^T\textbf{w}$ we can find an LS solution directly ( a closed-form LS solution ).
$$\textbf{w}^\pi = \argmin_\textbf{w} LS(\textbf{w})$$
It means that when we are at the minimum of LS, the expected update over the samples is equal 0
![[Pasted image 20260127093145.png]]
We need to invert a matrix but it does not depend any more on the number of states but on the N number of features that we are considering.
The **direct solution** is
- $O(N^3)$
- $O(N^2)$ using Shermann-Morrison

But we don't know the true value $v^\pi_t$ , we need to use biased or noisy samples of it:
- LSMC ( Least Square Monte Carlo) uses the return
$$v^\pi_t \approx G_t$$
- LSTD ( Least Square Temporal Difference) uses the TD return
$$v^\pi_t \approx R_{t+1} + \gamma \hat{v}(S_{t+1} , \textbf{w})$$
- LSTD($\lambda$) ( Least Square TD($\lambda$)) uses the $\lambda-$return
$$v^\pi_t \approx G_t^\lambda$$
![[Pasted image 20260127093724.png]]
Convergence Of Linear LS prediction algorithms:
![[Pasted image 20260127093807.png]]

## Least Square Control

### Least Squares Policy Iteration
It is used for solving the control problem by using Least Square approach.
The policy evaluation step is replaced with **least square Q-learning** while the policy improvement is always using a greedy policy improvement.
![[Pasted image 20260127094344.png]]

We want to approximate the action-value function $q_\pi(s,a)$ using linear combination of features $x(s,a)$
$$
\hat(q)(s,a,\textbf{w}) = x(s,a)^T \textbf{w} \approx q_\pi(s,a)
$$
We start from an experience which is again a dataset consisting of <(state,action), value> pairs
![[Pasted image 20260127094643.png]]
We want to minimise the least square error between the value function approximation $\hat{q}(s,a,\textbf{w})$ and true value $q_\pi(s,a)$ which is generated/sampled using policy $\pi$  from experience.

**Least Square Control** combines batch methods with off-policy learning:
- We want to use all the experience efficiently for policy evaluation
- We want to improve the policy for the control problem  
- But the experience comes from many different policies ( old data )
	- Each step we improve the policy, the old data stay related to the previous policy
	- For this reason we need to use off-policy learning ( learning from following a policy which is not the one that the agent is currently following )
How it works?
It uses the same approach of Q-learning but applied to batch data
- Use experience generated by old policy
$$S_t, A_t, R_{t+1}, S_{t+1} \sim \pi_{old}$$
- We consider alternative successor action 
$$A' = \pi_{new}(S_{t+1})$$
- We update our action-value function approximation $\hat{q}(S_t,A_t,\textbf{w})$ towards value of alternative action $R_{t+1} + \gamma \hat{q}(S_{t+1},A',\textbf{w})$
Update our estimate using the new policy's predicted value, not the old policy's.
![[Screenshot 2026-01-27 alle 10.03.52.png]]

### Least Square Q-learning
We can consider the following linear Q-learning update:
![[Pasted image 20260127100743.png]]
We can solve it directly instead of doing many iterations of SGD: Least Squares Temporal Difference Q-Learning (LSTDQ)( batch method that solves analytically instead of using gradient descent )
![[Pasted image 20260127100918.png]]

![[Screenshot 2026-01-27 alle 10.09.24.png]]

### Least Squares Policy Iteration Algorithm
It uses the LSTDQ algorithm for policy evaluation by repeatedly re-evaluating experience D with different policies.
![[Pasted image 20260127101127.png]]
How it works?
![[Screenshot 2026-01-27 alle 10.16.13.png]]
This was a **practical algorithm before deep RL** for problems with moderate state/action spaces. Modern deep RL (DQN) uses experience replay + gradient descent instead, which scales to high-dimensional problems.

Convergence of Control Algorithms:
![[Pasted image 20260127101706.png]]

# Policy Gradient
Instead of working with value functions as we have seen so far, we are working with the policy, how can i see some experience and from that figure out how to change my policy in a direction that makes it better.
We are improving the policy directly.

## Policy-Based RL
In the last lecture we approximated the value/action-value function using parameters $\theta$
$$
V_\theta(s) \approx V^\pi(s)
$$
$$
Q_\theta(s,a) \approx Q^\pi(s,a)
$$
And then we generated a policy directly from the value function using a $\epsilon-$greedy approach.
Now we will focus on model-free RL with **direct parametrization of the policy**
$$
\pi_\theta(s,a) = P[a | s,\theta]
$$
We are using $\theta$ and not $\textbf{w}$ for the parameters.
We are actually defining a probability distribution by which we are picking actions that's conditioned both on the state and our parameters.


## RL Categorization
There are three types of RL algorithms:
- Value based $\rightarrow$ we want to learn the value function ( indirectly we get the policy )
- Policy Based $\rightarrow$ we want to learn the policy directly without learning the value function
	- Advantages: 
		- Better converges properties
		- Effective in high-dimensional or continous action space
		- Can learn stochastic policies
	- Disadvantages:
		- Typically converge to a local rather than a global optimum
		- Evaluating a policy is typically inffecient and high variance
- Actor-critic $\rightarrow$  we learn both the value function and the policy
![[Pasted image 20260127112832.png]]

**Example 1**: Rock-Paper-Scissors
![[Pasted image 20260127114101.png]]
Rules:
- Scissors beats paper
- Rock beats scissors
- Paper beats rock
This is a case where the optimal behavior is actually stochastic: uniform random policy is optimal ( we exploit the Nash equilibrium, if we try to play a figure more than others our opponent will figure out and it will use it against us)

**Example 2**: Aliased Gridworld
![[Pasted image 20260127114315.png]]
We consider features of the following form ( for all N, E, S, W):
$$\phi(s,a) = 1(\text{wall to N} , \text{a = move E})$$
Is there a wall to the North when I try to move East? The agent can not differentiate the grey states ( they are identical to the agent ) due to these limited features
![[Screenshot 2026-01-27 alle 11.56.12.png]]
So the agent gets confused and can get stuck because it doesn't know it's in different positions.

We want to know what is the best i can do using either value based or policy based RL:
- Value-based RL, we parametrize the value function
$$
Q_\theta(s,a) = f(\phi(s,a), \theta)
$$
- Policy-based RL, we parametrize the policy
$$
\pi_\theta(s,a) = g(\phi(s,a),\theta)
$$

if you use a deterministic policy then you have to pick the same action in those two grey states: move W or E in both grey states.
![[Pasted image 20260127134337.png]]
Either way, it can get stuck and never each the money.
Value-based RL learns a **near deterministic policy** so it will traverse the corridor for a long time.
![[Pasted image 20260127134452.png]]
An optimal **stochastic** policy (which can be learnt by Policy Based RL ) will randomly move E or W in grey states:
![[Pasted image 20260127134512.png]]
It will reach the goal state in a few steps with high probability.

Whenever **state aliasing** occurs a stochastic policy can do better than a deterministic policy.

## Policy Evaluation through Policy Objective Functions
To optimize a policy ( the best parameters $\theta$) well we need to know that the objective should be.
In other terms how do we measure the quality of a policy $\pi_\theta(s,a)$ parameterized by $\theta$ for understanding how much good it is.
We have three different objective functions/metrics:
- In episodic environments we can use the **start value**
$$
J_1(\theta) = V^{\pi_\theta}(s_1) = E_{\pi_\theta}[v_1]
$$
We use it when an environment has a specific starting state (e.g. start of the game).
The value function $V^{\pi_\theta}(s_1)$ tells you: "If we start here and follow policy $\pi_\theta$, how much reward will we get?"
Core idea: Expected cumulative reward starting from the starting state.
- In continuing environments we can use the **average value**
$$
J_{avV}(\theta) = \sum_s d^{\pi_\theta}(s) V^{\pi_\theta}(s)
$$
In a continuing environment there might not be a start state ( it runs forever ).
$d^{\pi_\theta}(s)$ is the stationary distribution ( If you run the policy for a very long time (to infinity), the probability of being in any state s stabilizes to it )
Core idea: Expected average value across all states I visit

- In continuing environments we can also use **average reward per time-step**
$$
J_{avV}(\theta) = \sum_s d^{\pi_\theta}(s)  \sum_a \pi_\theta(s,a) R^a_s
$$
we care about getting the most reward per time step.
On average, per time-step, how much reward do I get?
$d^\pi_\theta(s)$ is stationary distribution of Markov chain for $\pi_\theta$  $\rightarrow$ you can think of d as "p generalized for any state space" - discrete or continuous

Core idea: If I follow this policy, what's the expected total reward I'll get?

The policy gradient is essentially the same for all of them ( they follow the same gradient direction but with some difference in terms of rescaling )

## Policy Optimization
We want to find the parameters $\theta$ that maximizes the objective function $J(\theta)$
There are many strategies but we will focus on methods based on gradient descent and methods that exploit sequential structure.

## Finite Difference Policy Gradient
We have an policy objective function $J(\theta)$ ( how much reward can i get out of this system ) and we want to make it higher: policy gradient algorithms search for a local maximum in $J(\theta)$ by ascending the gradient of the policy w.r.t parameters $\theta$
$$
\Delta \theta = \alpha \nabla_\theta J(\theta)
$$  
where:
-  $\nabla_\theta J(\theta)$ is the **policy gradient**
![[Pasted image 20260127143300.png]]
- $\alpha$ is a step-size parameter
Gradient **Ascent** ( and not descent how we have seen before ).
Finite Differences means estimating the k-th partial derivative of objective function w.r.t $\theta$ by perturbing $\theta$ in the k-th dimension of a small amount $\epsilon$ 
$$
\frac{\partial J(\theta)}{\partial \theta_k} = \frac{J(\theta + \theta u_k) - J(\theta)}{\epsilon}
$$
We look at our objective function and we estimate it numerically by saying what happens if i perturb my parameters a little bit in each dimension separately and i check the difference between the  objective function value with this perturbation and without. It gives us a numerical estimate of the gradient but it is naive and inefficient for high dimensional parameters ( it requires n evaluations for computing policy gradient in n dimensions ).
It is simple and works for arbitrary policies even if it is not differentiable.

## Monte Carlo Policy Gradient
We start with the easiest approach with no value functions yet.
We compute the policy gradient analytically.
We assume that:
- the policy $\pi_\theta$ is differentiable whenever it is non-zero ( so it has to be differentiable only when it is actually picking actions ) and 
- we know the gradient $\nabla_\theta \pi_\theta(s,a)$ of the policy ( it can be a softmax policy, a gaussian policy or a neural network ) and we know the gradient of this things because we have created it
	- In other terms we choose the distribution of the policy and for this reason we know its gradient.

We are going to use a trick called **Likelihood ratios**:
![[Pasted image 20260127145312.png]]
where $\nabla_\theta \log \pi_\theta(s,a)$ is called **score function**. 

We want to see what score function looks like for two common example:
1. Softmax policy $\rightarrow$ smoothly parameterized policy that tells us how frequently we should choose an action for each of our discrete set actions ( alternative to $\epsilon-$greedy)
	- The softmax is **smoother** and **differentiable**, which is crucial for gradient-based learning!
We are going to form some linear combination of features that tells us how much we'd like to take an action ( weights for actions )
The probability of picking an action is proportional to the exponentiated value that we get when we take a linear combination of these features 
$$
\pi_\theta(s,a) \propto e^{\phi(s,a)^T \theta}
$$
Its score function is:
$$
\nabla_\theta \log \pi_\theta(s,a) = \phi(s,a) - E_{\pi_\theta}[\phi(s,\cdot)]
$$
![[Screenshot 2026-01-27 alle 15.50.18.png]]
The feature for the action that we actually took minus the average feature for all the actions that we might have taken. 
If a feature occurs more than usual and it gets a good reward then we want to adjust the policy to do more of that.
![[Screenshot 2026-01-27 alle 15.51.46.png]]
![[Screenshot 2026-01-27 alle 15.52.13.png]]

2. Gaussian Policy  $\rightarrow$  in a continuous action space it is the common choice.
	1. We can parametrize the mean as a linear combination of state features and fix the variance $\sigma^2$ ( it can be also parametrized )
$$
\mu(s) = \phi(s)^T \theta
$$
$$
a \sim N(\mu(s),\sigma^2)
$$
The score function is :
$$
\nabla_\theta \log \pi_\theta(s,a) = \frac{(a-\mu(s))\phi(s)}{\sigma^2}
$$
It is very similar what we have seen previously: the action that we took minus the mean tells us how much more than usual we are doing a particular action , multiplied by the feature and than we just scale it by the variance.

In both of these cases the score function takes this form of how much more than usual i am taking a particular action 

### Policy Gradient Theorem
We are going to consider **one-step** MDPs: MDPs that start in some state $s \sim d(s)$ and you take one step with one reward $r=R_{s,a}$ and the episode terminates immediately ( there is no sequence in this case ).

We choose as objective function the last one ( expected reward of our policy ): we want to find the parameters which give us the most expected reward.
![[Pasted image 20260127160951.png]]
We want to compute gradient of it by using the likelihood ratios trick.
![[Pasted image 20260127161004.png]]
We take an expectation , we applied a gradient and we get something which is still an expectation.

We want to do the same things in multi-step MDPs: we defined the **Policy Gradient Theorem** which can be applied to all of the 3 policy objective functions seen previously.
![[Pasted image 20260127161756.png]]
We have just replaced instantaneous reward $r$ with long-term value $Q^\pi(s,a)$
It is the expectation over the score function multiplied by the action value function and it basically tells you how to adjust the policy to get more or less of that particular action multiplied how good that particular action was.

### Monte Carlo Policy Gradient Algorithm
It is very similar to an old algorithm called *reinforce*
The idea is to update parameters by stochastic gradient ascent using the policy gradient theorem. We want to get rid of that expectation by sampling $Q^\pi_\theta(s_t,a_t)$ ( which is the term that appears in the expectation ) as an unbiased return of $v_t$
$$
\Delta \theta_t = \alpha \cdot \nabla_\theta \log \pi_\theta (s_t,a_t)\cdot v_t
$$
![[Screenshot 2026-01-27 alle 16.30.23.png]]
![[Pasted image 20260127162539.png]]
We want to adjust our parameter towards a little bit in the direction of this stochastic gradient ( which is the score multiplied by the sample return from that step ).
![[Pasted image 20260127163517.png]]
It usually gives us a very nice smooth learning curve ( RL has more jaggy curves usually ) but it requires a lot of iterations to solve a problem ( in this example hundred million iterations ): Monte Carlo Policy Gradient is very slow and it tends to be very high variance.

## Actor-Critic Policy Gradient
Instead of using the return to estimate the action-value function we are going to explicitly estimate the action value function using a **Critic** ( value function approximator ).
$$
Q_w(s,a) \approx Q^{\pi_\theta}(s,a)
$$
Actor-critic algorithms maintain two sets of parameters:
- Critic $\rightarrow$ it updates action-value function parameters $w$
	- it watches what the actor does seeing whether that's good or bad evaluating that thing
- Actor $\rightarrow$ it updates the policy parameters $\theta$ in the direction suggested by critic
	- It is the thing which is doing things in the world 
The idea is to use an approximate policy gradient instead of the true policy gradient: we are going to adjust the policy in the direction which according to the critic will get more reward.
![[Pasted image 20260127164649.png]]

The critic is solving the policy evaluation problem that we have seen before: how good is policy $\pi_\theta$ for current parameters $\theta$?
We can use:
- Monte Carlo Policy Evaluation
- Temporal-Difference learning
- TD($\lambda$)
- Least-squares Policy Evaluation

### Action-Value Actor-Critic
This is a simple version of actor-critic algorithm based on action-value critic, we are using a linear value function approximation for it:
$$
Q_w(s,a) = \phi(s,a)^T w
$$
Linear combinations of features and weights
![[Pasted image 20260128090750.png]]
The critic is grounded in **real data** (the actual reward r and next state s'), while the actor trusts the critic's evaluation.
![[Screenshot 2026-01-28 alle 09.11.17.png]]
Approximating the policy gradient introduces bias and it may not find the right solution.
If we choose value function approximation correctly we can avoid introducing any bias:
![[Pasted image 20260128101725.png]]
This is the proof:
![[Pasted image 20260128101951.png]]

In order to **reduce the variance without changing the expectation** we subtract the function B(s) from the policy gradient.
![[Pasted image 20260128102802.png]]
If we add or subtract any term of this form we don't change the final expectation of the old formula.
A good baseline function is the state value function $B(S) = V^{\pi_\theta}(s)$
Therefore we can rewrite the policy gradient using the advantage function $A^\pi_\theta(s,a)$:
$$
A^{\pi_\theta}(s,a) = Q^{\pi_\theta}(s,a) - V^{\pi_\theta}(s)
$$
The gradient of the objective functions become:
$$
\nabla_\theta J(\theta) = E_{\pi_\theta}[\nabla_\theta \log \pi_\theta(s,a) A^{\pi_\theta}(s,a)]
$$
It tells us how much better than usual a particular action a is and how to adjust our policy to achieve that action a.
Instead of asking "how good is action a?" (Q-value), you ask "how good is action a compared to the average?" (advantage). This centers the signal and makes learning much more stable and efficient.
The state value function $V^\pi(s)$ is the perfect baseline because it literally represents what "usual" performance is in that state.
![[Screenshot 2026-01-28 alle 10.42.09.png]]
### Estimating the Advantage Function
The advantage function can significantly reduce variance of policy gradient.
The critic should approximate and update both using two function approximators  and two parameter vectors:
![[Pasted image 20260128104434.png]]
Assuming we know the true value function $V^{\pi_\theta}(s)$ , the TD error is defined as:
$$
\delta^{\pi_\theta} = r + \gamma V^{\pi_\theta}(s') -  V^{\pi_\theta}(s)
$$
**The TD error is an unbiased estimate of the advantage function**
![[Pasted image 20260128110256.png]]
We can use the TD to compute the policy gradient replacing the advantage function term in the definition:
$$
\nabla_\theta J(\theta) = E_{\pi_\theta}[\nabla_\theta \log \pi_\theta(s,a) \delta^{\pi_\theta}]
$$
In practise we can approximate the TD error by approximating only V using only one set of critic parameters V:
$$
\delta_v = r + \gamma V_v(s') - V_v(s)
$$
We have just rewritten the policy theorem gradient by approximating things.

### Critics at Different Time-Scales
We don't want always to go all the way into the end of the episode or just take only one step because that's biased.
We want to deal with bias and variance using different time-scals with actor critic algorithms.
The target for our updates can be many, just a recall from what we have seen:
![[Pasted image 20260128111148.png]]
We can do that with the critic but what about the actor? Can we plug in it a TD($\lambda$) learning algorithm?
We have seen two types of policy gradient up to now:
- Monte-Carlo policy gradient which uses error from complete return 
$$
\Delta \theta = \alpha(v_t - V_v(s_t)) \nabla_\theta \log \pi_\theta(s_t,a_t)
$$
- Actor-critic policy gradient which uses the one step TD error -> TD(0)
$$
\Delta \theta = \alpha ( r + \gamma V_v(s_{t+1}) -V_v(s_t) ) \nabla_\theta \log \pi_\theta(s_t,a_t)
$$

We can try to define a **policy gradient with Eligibiliy Traces** as we have done for value based reinforcement learning.
- Like Forward-view TD($\lambda$), we can mix over time-scales
$$delta \theta = \alpha (v_t^\lambda -V_v(s_t)) \nabla_\theta \log \pi_\theta(s_t,a_t)
$$
with $v_t^\lambda - V_v(s_t)$ is a biased estimate of advantage function

- Like Backward-view TD($\lambda$),  we can also use eligibility traces
![[Pasted image 20260128112707.png]]

This idea is useful for how to make our actor make use of critics from many different steps all the way into the future.
Unlike the MC we can apply it online in non-finite sequences.

### Natural Policy Gradient
Vanilla policy gradient updates parameters directly in parameter space:
$$
\theta \leftarrow \theta + \alpha \nabla_\theta J(\theta)
$$
This computes: _"If I change parameter θ₁ by a tiny amount, how much does my objective J improve?"
Let's suppose our policy is a Gaussian with mean $\mu$, we can parametrize it in two ways:
1. $\mu = \theta$
2. $\mu = 2\cdot \theta$ ( we are just scaling the parameter)
The **same policy** would produce different gradients in these two versions! It means that the directions changes:
![[Screenshot 2026-01-28 alle 11.49.59.png]]
The vanilla gradient depends on how you arbitrarily wrote down your equations, not on the actual policy behavior.
**Valilla gradient** is sensitive to these reparametrisations.
![[Pasted image 20260128115534.png]]
**Natural Policy Gradient** is pamametrisation independent : it moves in policy space instead.
$$
\nabla_\theta^\text{nat} \pi_\theta(s,a) = G_\theta^{-1} \nabla_\theta \pi_\theta(s,a)
$$
Where $G_\theta$ is the fisher information matrix
$$
G_\theta = E_{\pi_\theta}[ \nabla_\theta \log \pi_\theta(s,a) \nabla_\theta \log \pi_\theta(s,a)^T]
$$
It measures how much the policy distribution actually changes when you change the parameters.
![[Screenshot 2026-01-28 alle 11.56.14.png]]
If we want to reduce the variance we can use the compatible function approximation $\nabla_w A_w(s,a) = \nabla_\theta \log \pi_\theta(s,a)$ and the natural policy gradient simplifies to
![[Pasted image 20260128115905.png]]


## Summary of Policy Gradient Algorithms
The policy gradient has many equivalent forms:
![[Pasted image 20260128120159.png]]
Each one leads to a stochastic gradient ascent algorithm.
Critic uses policy evaluation to estimate Q , A or V.

# Integrating Learning and Planning

We have seen that there are two types of RL:
- Model-free RL $\rightarrow$ there is no model at all, the agent tries to learn the value function (and or policy) from experience.
	- The agent does not make any effort to explicitly represent the transition dynamic or the reward function that the environment is operating on
![[Pasted image 20260128134040.png]]
- Model-based RL $\rightarrow$ learn a model from experience.
	- It uses that model to **plan** a value function (and/or policy).
	- Plan means using a model to look ahead , to think, to compute , to figure out what the right value function or the rights actions are to select in this environment
![[Pasted image 20260128134101.png]]
We replace the world with the agent's model of the world.

## Model-Based Reinforcement Learning
In the previous lecture we learnt policy/value function directly from experience, in this case we want to learn model directly from experience and use planning to construct a value function or policy.
After that we want to integrate learning and planning into a single architecture.

A model , in this section, is something that describes  for any given environments the agent's understanding of that environment ( how states transition to other states and how states lead to rewards ).

![[Pasted image 20260128134724.png]]
From the interaction with the real world, we get experience which is useful to build up our model. We use our model to plan ( look ahead process ), the agent starts interacting with the world understanding of the agent. The interaction between the model and the agent generates a value function/policy which can be used to act in real world.

Advantages of model based RL:
- Can efficiently learn model by supervised learning methods
- Can reason about model uncertainty

Disadvantages:
- First learn a model and then we use that model to  construct a value function that means we have two sources of approximation error.

### Learning a Model
A model M is a representation of an MDP <S,A,P,R> parametrized by $\eta$, we will assume that state S and action A spaces are known.
So a model
$$
M = <P_\eta, R_\eta>
$$
represents state transitions $P_\eta \approx P$ and rewards $R_\eta \approx R$.
![[Pasted image 20260128135922.png]]
We typically assume that state transitions and rewards are independent:
![[Pasted image 20260128140118.png]]
Our goal is to estimate the model $M_\eta$ from experience {$S_1,A_1,R_2,...,S_t$}.
This is a supervised learning problem:
![[Pasted image 20260128140708.png]]
Taking an action $A_t$ while i am in the state $S_t$ will give me a reward of $R_{t+1}$ and i will end in a state $S_{t+1}$.
We collect all these examples that we see from all of our trajectories that gives us our training set which can be used to learn:
- The reward, which is a **regression** problem
$$
s,a \rightarrow r
$$
- The state, which is a **density estimation** problem
$$
s,a \rightarrow s'
$$
For both of them we should choose a proper loss function ( regression requires MSE and density estimation problem requires KL divergence ) and then find the parameters $\eta$ that minimize empirical loss.

Examples of models:
- Table Lookup Model
- Linear Expectation Model
- Linear Gaussian Model
- Deep Belief Network Model
- ecc...

#### Table Lookup Model
It is the simplest case.
The model is an explicit MDP $\hat{P}, \hat{R}$.
I just use the empirical count $N(s,a)$ visits to each state action pair to give me a probability distribution over we'll go next.
![[Pasted image 20260128141942.png]]
Alternatively:
- We just remembers things: at each time-step $t$ we record experience tuple $<S_t, A_t, R_{t+1} ,S_{t+1}>$.
- If we want to sample from this model , we just need to randomly pick a tuple matching the action and the state that we want to consider $<s,a,\cdot,\cdot>$

**Example** AB
![[Pasted image 20260128142429.png]]
We have two states A and B with no discounting and 8 episodes.
The right MDP is built by using a table lookup model from the experience.

### Planning with a Model
Planning means solving that MDP , we use that model that we have got to try and find the best thing to do.
Starting from a model
$$
M_\eta = <P_\eta, R_\eta>
$$
We want to solve the MDP
$$
<S,A,P_\eta,R_\eta>
$$
using our favoring planning algorithm:
- Value iteration
- Policy iteration
- Tree search
- ecc...

#### Sample-Based Planning
It is a simple but powerful approach to planning.
We use the model only for generating samples ( not as in Dynamic Programming where we want to know the probabilities behind ): we treat the model as it was the real world.
We sample experience from our model:
![[Pasted image 20260128151323.png]]
And then we apply model-free RL to these samples ( they form a dataset ):
- Monte-Carlo control
- Sarsa
- Q-learning

**Example** AB
We started from the real experience and we have generated a model ( we built a table-lookup model ).
We use the model to sample experience
![[Pasted image 20260128151740.png]]
We learn from our sampled experience by applying the Monte-Carlo Learning 

#### Planning with an Inaccurate Model
Supposing we are dealing with a in imperfect model 
$$
<P_\eta, R_\eta> \neq <P,R>
$$
The performance of model-based Reinforcement Learning is limited to optimal policy for the approximated/imperfect MDP that we are considering.
In other words , model-based RL is only as good as the estimated model.
When the model is inaccurate , planning process will compute a suboptimal policy, we can:
- Solution 1 $\rightarrow$ use directly model-free RL
- Solution 2 $\rightarrow$ reason explicitly about model uncertainty

## Integrated Architectures
We want to bring together the best of model-free and model-based RL trying to construct something which has the advantages of both.

We consider 2 sources of experience:
1. Real Experience  $\rightarrow$  Sampled from environment ( true MDP )
$$
S' \approx P_{ss'}^a
$$
$$
R = R_s^a
$$
2. Simulated Experience  $\rightarrow$ Sampled from model ( approximate MDP )
$$
S' \approx P_\eta(S' | S, A)
$$
$$
R = R_\eta(R | S,A)
$$

We can finally distinguish three types of RL:
- Model-free RL
- Model Based RL
- Dyna
	- We learn a model from real experience and we learn and plan value function ( and/or policy ) from **real and simulated experience**.

### Dyna Architecture
![[Pasted image 20260128155359.png]]
The ark here means that we are learning the value/policy both from simulated experience and real experience ( data from real world )
**Dyna-Q** algorithm:
![[Pasted image 20260128155650.png]]
We take a real action in the world and we update both the action-value function ( SARSA update ) and the model. ( d and e ).
Then we have the imagination/thinking loop which lasts for n steps , in each of it we sample an action A and a state S from real experience and i imagine to be in that state S and that i take that action S , i get from my model which is my reward R and next state S'. We apply then a q-learning step to that imagine transition in order to update our action-value function Q.
![[Pasted image 20260128162258.png]]
There are some variants of Dyna-Q algorithm that allows us to handle the situation where the environment learnt before is now different: the agent needs to explore m]ore , we have the Dyna-Q+ variant for that ( it gives a bonus for states that have not been visited yet , it is a way to motivate the agent exploration ).

## Simulation-Based Search
In this last section we are going to back off to just one part of model-based RL,  to the planning problem.
We are going to focus on how to plan effectively.

The key idea that we are going to use is sampling and forward search.

### Forward Search
Forward search algorithms select the best action by **lookahead**  , they don't explore the entire state space but  they focus on the particular current state ( focusing on what's likely to happen next in the short term future ).
They build a search tree with the current state $s_t$ at the root using a model of the MDP to look ahead
![[Pasted image 20260128163236.png]]
We don't need to solve the whole MDP but just sub-MDP that starts from now : instead of learning a policy over the entire state space, forward search asks: "From my current state s_t, what's the best action if I look ahead a few steps?"
![[Pasted image 20260128163554.png]]
Simulation based search is a **forward search paradigm** that uses sample-based planning: we start from now and we imagine what might happen next , we image a trajectory of experience by sampling it from our model.
![[Screenshot 2026-01-28 alle 16.44.23.png]]
Once you have these simulated trajectories, you apply standard RL algorithms (like Q-learning, policy gradient, etc.) on them as if they were real experiences ( we can use this as a training sample for your value function, just like a real transition )
![[Screenshot 2026-01-28 alle 16.51.37.png]]
Example:
![[Screenshot 2026-01-28 alle 16.53.24.png]]
**How it works?**
1. We simulate episodes of experience from now with the model: it means that we sample trajectories from our model
![[Pasted image 20260128165627.png]]
2. We apply model-free RL to these simulated episodes ( to these trajectories sampled from our models, simulated data not real one ).
	1. Monte-Carlo control that gives us a method called **Monte Carlo search**
	2. Sarsa that gives us a method called **TD search**

### Simple Monte-Carlo Search
This is the simplest version.
Considering a model $M_v$ and a simulation policy $\pi$ ( the way that we are picking up actions in our imagination )
For each action $a \in A$:
- We simulate K episodes from current ( real ) state $s_t$
![[Pasted image 20260128170254.png]]
*Simulate means sampling from our model/simulation/the way our agent sees the world*
- We evaluate each of these actions by mean return ( Monte-Carlo Evaluation )
![[Pasted image 20260128170353.png]]
At the end we select the current real action with maximum value
$$
a_t = \argmax_{a \in A} Q(s_t,a)
$$

### Monte-Carlo Tree Search
From our current state $s_t$, we use our model $M_{v,\pi}$ to imagine k complete episodes using current simulation policy $\pi$.
![[Pasted image 20260128171050.png]]
We build a search tree using all the states and actions that we visited in those K episodes.
![[Screenshot 2026-01-28 alle 17.12.19.png]]
Instead of just evaluating the root action-value function values, we are going to evaluate every state action pair that we visit by computing its Q value.

We evaluate states $Q(s,a)$ by mean return of episodes that pass through the pair (s,a)
![[Screenshot 2026-01-28 alle 17.13.01.png]]
where:
- $N(s,a)$ means how many times the couple (s,a) appeared across all k episodes
- $1(S_u, A_u = s,a)$ means "Did we visit state s and take action a at step u?"
- $G_u$ is the return from step u onward 
In simple terms: For each (state, action) pair in the tree, compute the **average return** you got when you were in that situation across all simulated episodes that pass through that pair in the tree.
After search is finished, the select the current (real) action with maximum value in search tree
$$
a_t = \argmax_{a \in A} Q(s_t,a)
$$
After every simulation we are going to make our simulations improve and we are doing it in the same way we did policy improvement:
Each simulation can be broken in two phases:
- In-tree / Tree policy $\rightarrow$ we pick actions to maximize Q(S,A)
	- We want to improve the policy
- Out-tree / Default policy  $\rightarrow$  when we are beyond my tree and i don't have anything stored , we just behave according to my some default random simulation policy ( which can be naive )
	- Pick actions randomly

The algorithm is ( for each simulation we repeat the following steps):
- Evaluate states Q(S,A) by Monte-Carlo Evaluation
- Improve the tree policy (e.g. using $\epsilon-$greedy(Q) )
This is basically **Monte Carlo Control** applied to simulated episodes of experience that start from the root state. 
It converges on the optimal search tree $Q(S,A) \rightarrow q_\star(S,A)$

##### Example Game of Go
Considered as the hardest classic board game and a grand challenge task for AI.
![[Pasted image 20260128173953.png]]
How it works?
- A board of 19x19 or 13x13 or 9x9
- Black and white take turns to place down the stone at some intersection
- There are two rules
	- If you completely surround a stone then it gets captured and removed from the board 
	- At the end of the game, the player with more territory wins the game 
- You want to place stones in the way that maximizes the amount of territory you get.

The reward function is defined as:
![[Pasted image 20260128174054.png]]
Every step that is intermediate gives no reward ( 0 ) and the final one gives 1 if black wins.
Our policy $\pi=<\pi_B, \pi_W>$ selects moves for both players.
The value function ( how good is position $s$) is defined as:
![[Pasted image 20260128174256.png]]
Value function : How much reward i get in average from this position
Optimal value function: min max problem.

We just apply the **Simple Monte Carlo Search** algorithm:
![[Pasted image 20260128174805.png]]
We are in a game position and we roll out some games using our simulation policy ( 4 different versions : in two of them i lost and in two i win).

We just apply the **Monte-Carlo Tree Search** algorithm:
![[Pasted image 20260128175103.png]]
![[Pasted image 20260128175236.png]]
We run two simulations from the root (current state ) to the end and we we save the results in the root ( we have gone through 2 results and we have one victory and one defeat 1/2).
We do it by starting from the new nodes and so on by updating everything:
![[Pasted image 20260128175500.png]]
![[Pasted image 20260128175600.png]]
![[Pasted image 20260128175544.png]]
It just explores the good trajectories ( the one with best results, it avoids the trajectories from 0/1 for example): the assumption is that the unique sample of that trajectory is sufficient to understand how good it is going through that state

Advantages of MCTS:
- Highly selective best-first search 
- Evaluate states dynamically ( unlike DP which requires a full view of the all state space )
- Use sampling to break curse of dimensionality
- Works for black box models
- Computationally efficient , anytime and parallaleisable

### TD Search
We want to use TD instead of MC bootstrapping: TD search applies to SARSA to sub-MDP from now.
Why should do we this?
- For model-free RL , bootstrapping is helpful
	- TD learning is more efficient than MC and reduces variance increasing the bias.
	- TD($\lambda$) can be much more efficient than MC
- For simulation-based search,  , bootstrapping is also helpful
	- TD search is more efficient than MC search and reduces variance increasing the bias.
	- TD($\lambda$) search can be much more efficient than MC search 

Algorithm:
- We start simulating episodes from our real current state $s_t$
- We now estimate our action-value function Q(s,a).
- For each step of simulation we update our action-value function by Sarsa
$$
\Delta Q(S,A) = \alpha ( R + \gamma Q(S', A') - Q(S,A))
$$
- We select actions by acting greed w.r.t our action-values $Q(s,a)$
The unique thing that changes w.r.t. Monte Carlo Search is that way we update our action-value function by using temporal differences.

#### Dyna-2
We want apply the DYNA algorithm ( combines both real and simulate experience ) with forward search algorithm.
Dyna-2 maintains two value functions with two sets of feature weights:
- Long-Term memory wihch is updated from real experience using TD learning
- Short-term ( working ) memory which is updated from simulated experience using TD search
We sum these two together to give us our overall value function.
![[Pasted image 20260129104632.png]]


# Exploration and Exploitation
Every time we are decision-making online , the same choice comes up again and again:
- Exploitation $\rightarrow$ make the best decision given current information
- Exploration  $\rightarrow$ do something gathering more information
The best long-term strategy may involve short-term sacrifices ( we choose exploration over exploitation ) in order to gather enough information to make the best overall decision.

Examples:
![[Pasted image 20260129110207.png]]

Exploration and Exploitation approaches:
- Naive Exploration $\rightarrow$ explore random actions / add noise to greedy policy ($\epsilon-$greedy)
- Optimistic Initialisation $\rightarrow$  assume the best until proven otherwise
- Optimism in the Face of Uncertainty $\rightarrow$  prefer actions with highest uncertainty 
	- If I'm uncertain, try it!
- Probability Matching $\rightarrow$  select actions according to probability they are best
	- Pick action with highest probability of being best
- Information State Search $\rightarrow$  lookahead to see how information helps reward 
	- Correct but computationally very difficult because our state space blows up to something massively more complicated that we had before.
	- It asks: what action gives me the most reward **AND teaches me something useful**?
![[Screenshot 2026-01-29 alle 11.18.54.png]]
![[Screenshot 2026-01-29 alle 11.29.32.png]]

## Multi-armed bandit
![[Pasted image 20260129113622.png]]
Multi-armed bandit is basically a simplification of the mdp framework where we just have a set of $m$ actions/arms A and a reward function R, we throw away the value space and the transition function.
$$
<A,R>
$$
Reward function is an unknown probability distribution over rewards: given an action/arm what distribution over reward we get with that machine.
$$
R^a(r)= P[R=r | A=a]
$$
At each step $t$ the agent selects an acton $A_t \in A$ and the environment generates a reward $r_t \sim R^{a_t}$ and our goal is to maximise cumulative reward
$$
\sum_{\tau=1}^t r_\tau
$$
### Regret
- The action-value is the mean reward for action a:
$$
Q(a) = E[r|a]
$$
No value here.
- The optimal value $v_*$
$$
v_* = Q(a^*) = \max_{a \in A} Q(a)
$$
- The regret is the opportunity loss for ones step 
$$
I_t = E[v_* - q(A_t)]
$$
It tells us how much worse we do than $v_*$ : in some step we don't do the best choice and we want understand the opportunity loss ( the difference between the maximum we could have got at that step and the actual action function value )

- The total regret is the total opportunity lost
$$
L_t = E\left[\sum_{\tau=1}^t v_* - q(A_\tau)\right]
$$
Maximizing the cumulative reward is equal to minimize the total regret.

The regret  can be also expressed as a function of gaps and counts:
- The gap $\Delta_a$ is the difference in value between some action a and the optimal action $a*$ 
$$
\Delta_a = V^* - Q(a)
$$
The gap between the best machine i could have pulled and some suboptimal machine.
- The count $N_t(a)$ is expected number of selections for action a
	- How many times you use that machine.

We can rewrite the regret as:
![[Pasted image 20260129120928.png]]
Good algorithms should ensure small counts for large gaps but the problem is that we don't know gaps ( $v_*$ is not known ).

How this regret look like over time by considering our familiar algorithms?
![[Pasted image 20260129132730.png]]
Randomly picking among our actions means that these actions can introduce some opportunity loss and:
- if an algorithm forever explores ,  it will have linear total regret ( greedy algorithm , blue line)
-  if an algorithm never explores ,  it will have linear total regret ( $\epsilon-$greedy algorithm , blue line)
We want to achieve sublinear total regret ( black line ).

### Greedy Algorithm
We will consider algorithms that estimate action-value function $Q_t(a) \approx q(a)$  and i want to estimate the value of each action by Monte-Carlo Evaluation
$$
Q_t(a) = \frac{1}{N_t(a)} \sum_{t=1}^T 1(a_t=a)r_t
$$
The greedy algorithm just selects action with highest value
$$
a_t^* = \argmax_{a \in A} \hat{Q_t}(a)
$$
Greedy algorithm can lock into suboptimal action forever and it has linear total regret.

### $\epsilon-$Greedy Algorithm
It works in this way:
- We select the best action $1 = \argmax_{a \in A} \hat(Q(a))$ with probability $1-\epsilon$
- We select a random action with probability $epsilon$
It continues to explore forever and the constant $\epsilon$ ensures minimum target
$$
I_t \geq \frac{\epsilon}{A} \sum_{a \in A} \delta_a
$$
It has linear total regret

### Decaying $\epsilon_t -$Greedy Algorithm
If we just decay our epsilon over time: we gradually reduce the value of a parameter over time or iterations during training or optimization.
Examples of decay strategies
![[Screenshot 2026-01-29 alle 13.54.41.png]]
We will consider the following schedule:
$$
\begin{aligned}
c &> 0\\
d &= \min_{a| \Delta_a > 0} \Delta_i\\
\epsilon_t &= \min\left\{1, \frac{c |A|}{d^2 t}\right\}
\end{aligned}
$$
This algorithm has logarithmic asymptotic total regret but It can not be used in practise because it requires knowing $v_*$ ( in the definition of gap ) in advance.
We want to find an algorithm with sublinear regret  ( like this ) for any multi-armed bandit without requiring the knowledge of R.

### Lower Bound
There is a theorem that says no algorithms can do better than a certain lower bound.
We want to push closer and closer towards this lower bound.
The lower bound is actually logarithmic in number of steps.
![[Pasted image 20260129141438.png]]
In general the performance of an algorithm depends on how much the optimal arm/action is similar to the others , the hardest problems are the one where we have similar-looking arms ( measured using the KL divergence $KL(R^a  || R^a_\star$ ) with different means ( using gaps $\Delta_a$ )
![[Screenshot 2026-01-29 alle 14.15.51.png]]

### Upper Confidence Bound UCB
We are going to use the strategy of **Optimism in the Face of Uncertainty**: let's suppose there are 3 different arms ( blue, red and green ) and we have 3 distribution over the actual Q values ( our belief ) with a mean that can be seen on the x axis.
![[Pasted image 20260129142506.png]]
Which action/arm/distribution we pick?  This principle says to do not take the one you currently believe is best ( green one ) but take the one which has the most potential to be the best ( blue one has the most potential to actually have a mean which is somewhere to the full right close to 3 or 4 ).
![[Pasted image 20260129142802.png]]
After picking blue action few times, our beliefs/distributions are changed and now we will about to select another action/arm/distribution which has much more potential and this process goes further until we get the best action.
We will use the general idea called **Upper Confidence Bounds**: we want to estimate an upper confidence $\hat{U_t}(a)$ for each action value in order that we have $Q(a) \leq \hat{Q_t}(a) + \hat{U_t}(a)$ with high probability ( it is the tale of the distribution what we just looked at ).
We don't want to estimate only the mean of the distribution but the mean + something in order to be in the tale of the distribution.
$\hat{U_t}(a)$ depends on th number of times $N(a)$ that action has been selected:
- If we selected it few times we have a small $N_t(a)$ and we will have a large $\hat{U_t}(a)$ ( the distribution will be wider due to uncertainty )
	- The Q value generated is uncertain ( the upper bound is very high )
- If we selected it a lot of times we have a big $N_t(a)$ and we will have a small $\hat{U_t}(a)$ ( the distribution will be narrower due to much more certainty )
	- The Q value generated is accurate ( the upper bound is so small that it is correct )
We want to select the action that maximizes the Upper Confidence Bound UCB
$$
a_t = \argmax_{a\in A}\left(\hat{Q_t}(a) + \hat{U_t}(a)\right)
$$

#### Hoeffding's Inequality
It is a statistical theorem that says:
![[Pasted image 20260129171641.png]]
We can bound this probability with that term and this is true for any distribution.
We apply this theorem to the bandit case: 
$$
P[Q(a) > \hat{Q_t}(a) + U_t(a)] \leq e^{-2 N_t(a) U_t(a)^2}
$$
#### Calculate UCB
We pick a probability p that true value exceeds UCB ( that we make a mistake ) and we solve the Hoeffding's Inequality for $U_t(a)$:
![[Pasted image 20260129173324.png]]
As we pick things more and more, the bonus term is going to get lower ( $N_t(a)$ is at the denominator ) and the opposite is also true.
We don't fix $p$ to a specific value ( e.g. 95% ) instead we slowly increase $p$ over time to be more and more confident that we have included the true Q value in our interval.
$$
p = t^{-4}
$$
$$
U_t(a) = \sqrt{\frac{2\log t}{N_t(a)}}
$$

#### UCB1 Algorithm
Every step we estimate our Q values by taking this Monte Carlo estimate ( empirical mean ) and we add the bonus term which only depends on the number of time steps and the number of times our agent picked that specific action. We pick the action with the highest total value:
$$
a_t = \argmax_{a \in A}\left\{ Q(a) + \sqrt{\frac{2\log t}{N_t(a)}} \right\}
$$
The UCB1 algorithm achieves logarithmic asymptotic total regret:
$$
\lim_{t \rightarrow \infty} L_t \leq 8 \log t \sum_{a | \Delta_a> 0} \Delta_a 
$$

### Bayesian Bandits 
We can consider a **bayesian approach** to the **multi-armed bandits with upper confidence idea**.
Bayesian bandits exploit prior knowledge of rewards: we want to make an assumption about the reward distribution $p[R^a]$. 

We consider a distribution $p[Q | \w]$  over action-value function with parameter $\w$ ( the parameters can be independent gaussian parameters for each of our arm/action $\w = [\mu_1 , \sigma^2_1 ,.. , \mu_k . \sigma_k^2$ for  $a \in 1,k]$).
Bayesian methods compute posterior distribution over the parameters $\w$ given the rewards seen so far
$$
p[\w | R_1, . . . , R_t]
$$
We use this posterior distribution to guide exploration:
- Upper Confidence Bounds ( Bayesian UCP )
- Probability Matching ( Thompson sampling )
We got better performance if prior knowledge is accurate.

#### Bayesian UCB
![[Pasted image 20260130100405.png]]
- First of all we compute our posterior given the data seen so far
$$
p[\w | R_1 , . . . , R_{t-1}]
$$
We can do it by applying the bayesian law $p[Q(a) | R_1, . . . , R_{t-1}] = p[Q(a) | \w] \cdot p[\w | R_1, . . . , R_{t-1}]$.
- We estimate the upper confidence from posterior
$$
U_t(a) = c \sigma(a)
$$
Where $\sigma(a)$ is the standard deviation of $P(Q(a) | \w)$ ( we move using multiples of the standard deviation to reach a specific point close to the tail )
- We pick the action that maximizes $Q(a) + c \sigma(a)$

#### Thompson Sampling
Instead of the upper confidence bound idea, we can apply **probability matching**: it selects an action $a$ according to probability that $a$ is the best one.
In other words it selects actions based on how often each option is optimal, rather than always choosing the single best option.
$$
\pi(a)$ = P\left[ Q(a) = \max_{a'} Q(a') | R_1, . . . , R_{t-1} \right]
$$
The probability you choose action $a$ equals the probability that $a$ is actually the optimal action, given the rewards you've observed so far.
When you're uncertain about which action is truly best, some uncertain actions might have a higher probability of being optimal than you realize
Probability matching allocates some tries to these uncertain actions based on their potential optimality. However, this can be **inefficient** because you're wasting attempts on suboptimal actions instead of consistently exploiting the best one.
it's hard to compute $\pi(a)$ analytically from the posterior distribution—meaning in practice, you'd need numerical methods or approximations to actually calculate these probabilities from your observed data.

**Thompson Sampling** is sample-based probability matching algorithm for multi-arms bandits:
$$
\pi(a) = E\left[ \textbf{1}\left(Q(a) = \max_{a'} Q(a')\right) | R_1, . . . , R_{t-1} \right]
$$
It uses the bayes law to compute posterior distribution
$$
p_\w(Q | R_1, . . . , R_{t-1})
$$
The is that : every step we sample the action-value function Q(a) from our posterior and we select the action maxisimising the sample $A_t = \argmax_{a \in A} Q(a)$.
Thompson sampling works for every type of distribution but for a specific class of problem , for Bernoulli bandits, it achieves Lai and robbins lower bound on regret.

### Information State Search
Exploration is useful because it gains information and if we try to quantify the value of the information that we got we can trade it perfectly:
- How much reward a decision maker would be prepared in order to have that information.
- Value of information is trying to quantify the value in terms of units of reward of actually taking an exploratory action
We can think of this as the difference between the long-term reward after getting information and the immediate reward.
We want to explore uncertain situations more but in an optimal way in order to reach an optimal trade off  between exploration and exploitation.

We are going to transform our Bandit problem ( seen so far as a one-step decision making problem ) back into an mdp ( into a sequential decision making problem ).
We are keeping at each state an *information state $\tilde{s}$* which is a statistic of the history ( $\tilde{s_t} = f(h_t)$ ) that summarizes all information accumulated so far ( e.g. i have pulled this lever 3 times and this lever 5 times ).
Each action $a$ causes a transition to a new information state $\tilde{s}'$ with probability $\tilde{P}^a_{\tilde{s} \tilde{s}'}$ ( e.g. i pulled the livers 3 times and 5 times and i pull the second liver again, i will end in a new information state where i have pulled the livers 3 times and 6 times ): we are transitioning from information state to information state.
We have a very large mdp because it contains all the possible information states:
$$
\tilde{M} = < \tilde{S}, A, \tilde{P}, R, \gamma >
$$

**Example:** Bernoulli Bandits
A Bernoulli bandit is a multi-armed bandit where each arm has a hidden probability of success.
Each arm $a$ has an unknown probability $\mu_a$ (e.g., arm 1 gives reward 1 with probability 0.3, arm 2 gives reward 1 with probability 0.7, etc.)
![[Screenshot 2026-01-30 alle 12.18.42.png]]
The information state , in this example, is $\tilde{S} = <\alpha, \beta>$ where:
- $\alpha_a$ counts the pulls of arm $a$ where reward was 0
- $\beta_a$ counts the pulls of arm $a$ where reward was 1

We formulated the bandit as an **infinite MDP** over information states which can be resolved using RL, we can apply:
- Model-free RL (e.g. Q-learning )
- Bayesian model-based RL (e.g. Gittins indices )
	- This approach is known as **Bayes-adaptive** RL which finds a bayes-optimal exploration/exploitation trade-off with respect to prior distribution

**Example:** Bayes-Adaptive Bernoulli Bandits
![[Pasted image 20260130140557.png]]
We start with some $Beta(\alpha_a, \beta_a)$ prior over reward function $R^a$.
Each time $a$ is selected we update the posterior for $R^a$
![[Pasted image 20260130140535.png]]
We define two counters: succeed counter and failure counter.
This defines transition function probability $\tilde{P}$ for the Bayes-adaptive MDP where the information state $<\alpha,\beta>$ corresponds to reward model $Beta(\alpha,\beta)$ and each state transition corresponds to a Bayesian model update.
![[Pasted image 20260130140916.png]]
This Bayes-Adaptive MDP can be solved by dynamic programming  through the **Gittings index algorithm**. Exact solution to Bayes-adaptive MDP is typically impossible due the size of the information state space ( it is too large ).

### Summary
![[Screenshot 2026-01-30 alle 14.15.07.png]]
All the ideas seen here can be extended to the mdp case