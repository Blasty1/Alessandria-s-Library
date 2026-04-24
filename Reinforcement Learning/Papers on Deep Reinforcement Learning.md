# An advanced learning environment and a scalable deep reinforcement learning approach for rolling stock circulation on urban rail transit line

Link:[https://www.sciencedirect.com/science/article/pii/S0968090X24004972?utm_source=chatgpt.com](https://www.sciencedirect.com/science/article/pii/S0968090X24004972)
Date: 16 Mat 2025

**Problem Description**
The rolling stock circulation (RSC) problem is to assign a fleet of rolling stocks to all the determined train trips throughout the operation horizon on an urban rail transit line. Given a set of timetabled trips to be implemented in a day, and a fleet of rolling stocks stored in the depot(s), the rolling stock circulation aims to guarantee all train services served by a rolling stock. In this paper, **the objective of rolling stock circulation includes minimizing the number of rolling stocks in utilization, balancing the workloads of rolling stocks, and balancing the inbound and outbound rolling stocks of the depot(s).** The sequence of train trips associated with a rolling stock corresponds to the possible workload in a day for the rolling stock, and should satisfy the sequencing constraints. For each pair of consecutive train trips in the sequence, the elapsed time from the arrival of the preceding train trip to the departure of the subsequent train trip must be no less than the minimum turnaround time. To facilitate the mathematical model, the following assumptions are introduced.
- Assumption 1: The timetable of train trips is predetermined and does not change when optimizing rolling stock circulation.
	- It means that, the departure times at the origin and the arrival times at the destination of all train trips are all determined and considered as the input for planning rolling stock circulation. Cancellation of train trips is not allowed when planning the rolling stock circulation. This is a basic assumption and consistent with reality.
- Assumption 2: The depots have sufficient tracks for retaining and maintaining rolling stocks, which means that each depot can accommodate all rolling stocks if necessary. This is not a limiting assumption as the depots are usually designed with sufficient capacity for long-term operation.
- Assumption 3: The turnaround tracks are assumed to be located outside the depot but near it. To reverse the operation direction, rolling stocks can either use the turnaround track or return to the depot and then start the service in the opposite direction. The latter operation, involving entering and exiting the depot, is regarded as a turnaround but with a longer duration. The capacity of turnaround facilities is considered sufficient. Multiple rolling stocks are allowed to operate at the same turnaround facility, but have to meet the safety headway constraint.
- Assumption 4: The number of depots is not necessarily only one. With multiple depots along the urban rail transit line, the rolling stocks are assumed to return to the nearest depot after serving all trips. Empty movements between depots will increase the operation cost, thus it is not allowed in our consideration.

**State/Observation Space:**
The state contains the information that the agent receives from the learning environment, representing the current status at time step 𝑡in reinforcement learning. For the rolling stock circulation problem on an urban rail transit line, the DRL agent makes a decision to assign a rolling stock to a specific train trip, according to the status of rolling stocks.
The global state $s^t$ at time step $t$ in DRL algorithm for rolling stock circulation is defined as the representation of all rolling stock statuses at the current time step $t$
$$
s^t = {s_k^t , k \in K}
$$
The local state of rolling stock $k$ at time step $t$ is defined as :
$$
s_k^t = \left(n_k^t , \bar{c}_k^t, \bar{b}_k^t , f_k^t \right)
$$
Where:
- The number of assigned train trips $n_k^t \rightarrow$   It records the total number of served train trips since the rolling stock $k$ departs from the depot.
- The remaining in-service time $\bar{c}_k^t \rightarrow$ Every rolling stock has a maximum allowed service time before it needs maintenance ( called $C_k$)
	- This attribute tracks how much of that budget is _left_. Each trip consumes time equal to its duration (departure time minus arrival time). Once this hits zero, the train can't take more trips.
- The remaining out-of-depot time $\bar{b}_k^t \rightarrow$ There's also a maximum total time a rolling stock can stay _outside the depot_ (called $B_k$), which includes both travel time and waiting/connection time between trips. This attribute tracks what's left of that budget.
- Elapsed turnaround time $f_k^t \rightarrow$ When a rolling stock finishes a trip, it needs to physically turn around at the terminal before it can serve the next trip in the opposite direction. This takes a minimum amount of time ($\Delta$). This attribute records _how long_ the train has been waiting/turning around.
	- If $f_k^t \geq \Delta$, the train is ready for its next trip; otherwise it still needs more time.
- Operation direction $o_k^t \rightarrow$ Simple binary flag: 0 = going one way, 1 = going the other way (e.g., uptown vs. downtown). Every time the rolling stock completes a trip, its direction flips. The agent needs this to know which trips are physically possible to assign next.
- Latest trip index $g_k^t \rightarrow$ This records _which trip_ the rolling stock is currently serving or just finished. It's basically a pointer to the timetable. If the train hasn't left the depot yet, it's set to -1 as a special "idle at depot" signal.
At every decision moment, the AI agent looks at these 6 numbers for _every_ rolling stock and uses that combined picture to decide which train to assign to the next upcoming trip. The goal is to keep service running without violating the maintenance/time limits.

**Action space:**
At time step $t$ in DRL, the agent executes an action $a^t \in A$ to select a rolling stock from the fleet of rolling stocks dedicated to the urban rail transit line. The action space is a set of actions, defined as $A = \{1,2,..., |K|\}$. The DRL agent executes action at each
origin departure time of all train trips, thus an action executed means a rolling stock is assigned to the current train service. Only one rolling stock is assigned to a train trip at each time step.
When assigning rolling stocks, the DRL agent can choose any rolling stock. However, penalties are set for the DRL agent if an unavailable rolling stock is selected. The unavailable rolling stocks include the one currently serving another train service and the one not finishing the turnaround operation.

**Environment dynamics:**
At time step $t$, the agent decides the action $a^t$ and assigns one rolling stock $a^t = k$ to the current train service $i^t$. Based on the global state $s^t$ at time step $t$, the next state $s^{t+1}$ can be obtained by the state transition dynamic $s^{t+1} \sim P(s^t, a^t)$.
The learning environment first determines the set of available rolling stock ($K^t \subseteq A$) at the time step $t$ for the current train service $i^t$.
The rolling stock can be seen as a candidate if it meets these 3 conditions:
1. The rolling stocks are not serving passengers or turning around at time step 𝑡, which are categorized into two types, the rolling stocks staying at the depot and the ones finished the turnaround operation at time step $t$ after serving a train trip(i.e. the elapsed turnaround time $f_t^k$ no less than the turnaround time limit  $\Delta$
2. The rolling stocks, have the operation direction $o_k^t$consistent with that of the current train service $i^t$ at time step $t$;
3. $\hat{b}_k^t$ and $c_k^t$ must be larger than the trip time of current train service $i^t$
The state transits when the agent decides the right action
$$
a^t = k , a^t \in K^t
$$
The current train trip $i^t$ will be served by rolling stock $k$ and accordingly the local state $s_k^t$ of rolling k updates to $s_k^{t+1}$:
$$
\begin{aligned}
n_k^{t+1} &= n_k^t + 1 \\[6pt]
\bar{c}_k^{t+1} &= c_k^t - (m_{i^t}^+ - m_{i^t}^-) \\[6pt]
\bar{b}_k^{t+1} &= \bar{b}_k^t - (m_{i^t}^+ - m_{i^t}^-) \\[6pt]
f_k^{t+1} &= 0 \\[6pt]
o_k^{t+1} &= 1 - o_k^t \\[6pt]
g_k^{t+1} &= i^t
\end{aligned}
$$
N.B. $m_i^+$ is the departure time of train trip $i$ and $m_i^-$ is the arrival time of train trip $i$.
For the rolling stocks **available but not selected** ($\forall k \in K , k \neq a^t$), they change only elapsed turnaround time $f_k^{t+1}$ and the remaining out-of-dep time $\hat{b}_k^{t+1}$
$$
\begin{aligned}
n_k^{t+1} &= n_k^t \\[6pt]
\bar{c}_k^{t+1} &= \bar{c}_k^t \\[6pt]
o_k^{t+1} &= o_k^t \\[6pt]
g_k^{t+1} &= g_k^t \\[6pt]
f_k^{t+1} &= \begin{cases} 0, & n_k^t = 0 \\ m_{i^{t+1}}^+ - m_{g_k^t}^-, & n_k^t > 0 \end{cases} \\[6pt]
\bar{b}_k^{t+1} &= \bar{b}_k^t - (f_k^{t+1} - f_k^t)
\end{aligned}
$$
How it works in practise the system?
![[Screenshot 2026-02-18 alle 12.05.33.png]]
Read from top to below, try to read step by step this figure, focus on details.
![[Screenshot 2026-02-18 alle 12.06.37.png]]

**Reward Function:**
The agent assigns rolling stocks one trip at a time, and only after all trips are assigned do you know the final quality ( how many trains were used, fairness, etc. ).
There are two rewards:
1. Step-wise reward $r'$  aims to reduce the number of rolling stocks used and to improve the rolling stock utilization rate.
2. Final reward $r$ given once, when all train trips have been assigned. It reflects the true objective: minimize total trains used, minimize depot deviation, maximize fairness.
**Step-wise reward $r'$**: 
It aims to reduce the number of rolling stocks used and to improve the rolling stock utilization rate.
It is the sum of 5 items, formulated as:
$$
r' = - \alpha'_1 r_a - \alpha'_2 r_n - \alpha'_4 r_w + \alpha'_4 r_v + \alpha'_5 r_o
 $$
 where:
 - $\alpha'_1 ,\alpha'_2, \alpha'_3, \alpha'_4, \alpha'_5$ are binary indicators ( 1 or 0 if the corresponding situation occurs )
 - If the agent unnecessarily pulled a new rolling stock from the depot, it gets a penatly $r_a$ 
 - If the agent violated a constraint, it gets a penalty $r_n$ or $r_w$
 - If the agent picked a rolling stock that had been waiting a long time, it gets a bonus $r_v$
 - If the agent picked an available stock correctly, it gets a bonus $r_o$
**Final Reward $r$**:
It tries to minimize the objective function $Z$ which is defined as:
$$
Z = w_1 \frac{z_1 - z_1^{min}}{z_1^{max} - z_1^{min}} + w_2 \frac{z_2 - z_2^{min}}{z_2^{max} - z_2^{min}} + w_3 \frac{z_3 - z_3^{min}}{z_3^{max} - z_3^{min}}
$$
where:
- $z_1$ counts how many rolling stocks are actually deployed 
	- you want it as small as possible
$$
z_1 = \sum_{e \in E^+} \sum_{k \in K} \eta^k x_e^k
$$
where $\eta^k$ is the cost of using rolling stock $k$ and $x_e^k$ is a binary variable to check if rolling stock k has been used in trip $e$
- $z_2$ At each depot, it compares how many rolling stocks **enter** vs **leave** during the day. Ideally these should be equal — you want the same number of rolling stocks at each depot at the end of the day as at the start, so maintenance planning for the next day is not disrupted. The absolute value captures the imbalance in either direction
$$
z_2 = \sum_{d \in D} \left| \sum_{k \in K} \sum_{e \in \delta_d^+} \eta^k x_e^k  - \sum_{k \in K} \sum_{e \in \delta_d^-} \eta^k x_e^k \right|
$$
- $z_3$  is essentially a standard deviation of workload across rolling stocks of the same type $h$ . $b_k$ is the out-of-depot time of rolling stock $k$ (a proxy for how hard it worked). The formula penalizes situations where some rolling stocks are overworked while others barely do
Since each term ( $z_1, z_2, z_3$ ) has completely different scales and units, we can not add them directly: each term is normalized to $[0,1]$ by subtracting its minimum and dividing by its range.
The weights reflect how much the operator cares about each objective with $w_1 + w_2 + w_3 = 1$.

The model aims to minimize the number of rolling stocks in utilization, the imbalance of the rolling stock number in depts during the operation horizon and the workload deviation of the rolling stocks in utilization.

**Algorithm:**
![[Screenshot 2026-02-18 alle 13.37.07.png]]
The algorithm can be decomposed into two processes, simulation and training. In the simulation process, the agent uses the new updated policy to interact with the learning environment, and generates experiences into a replay buffer. In the training process, the replay buffer releases a batch experience to the actor network and critic network for their updates. The critic network generates an advantage function for the actor network, and it updates with the randomly sampled experience from the batch. When the actor network receives the advantage function, it updates according to the advantage function and the same randomly sampled experience.

**Deep neural network architecture:**
PPO is an actor-critic algorithm which means:
- Actor network is a policy function $\pi$ with parameters $\theta$ , the input of the NN is the global state $s^t$ and the output is the logit probabilities of each action in the optional action set A.
$$
a^t \sim \tau^t = \pi_\theta(s^t)
$$
- Critic network is a value function $\varphi$ with parameters $\rho$. The input is the global state $s^t$ and the output is the estimation value of the global state $v^t$ defined as
$$
v^t = \varphi_\rho(s^t)
$$
The architectures of the actor network and critic network are shown in Figs. 3(a) and 3(b) respectively. For the actor network, the first layer is the input layer which receives the global state $s^t$, the second and third layers are hidden layers with hyperbolic tangent function (Engstrom et al., 2020) as activation function, and the last layer is the output layer which returns the logit probabilities (choosing preference) of actions. Each two adjacent layers of the four are fully connected linear layers. For the critic network, the overall architecture of the first three layers is the similar to the actor network, but the last layer has only one neuron and returns the estimated value.

**Simulation Process:**
At the beginning of each episode in the simulation process, the learning environment is reset with the initial state $s^0$, and the actor network $\pi$ and critic network $\phi$ are initialized with parameters $\theta_0$ and $\rho_0$, respectively. In the simulation, the agent first chooses an action according to the state, as following:
$$
\begin{align}
\mu^t = \Psi(\tau^t)\\
a_t = \phi(u^t)
\end{align}
$$
$\mu^t$ is the categorical distribution obtained by applying the categorical distribution function  $\Psi$ to our set of probabilities $\tau$ at time $t$.
$\phi$ is the random sampling function: in other words it samples an action from the categorical distribution defined with our probabilities.



# Designing Rewards for Fast Learning

Link:https://arxiv.org/pdf/2205.15400
Date: 30 May 2022

Firstly, we advocate choosing state-based rewards that maximize the action gap, making optimal actions easy to distinguish from suboptimal ones. Secondly, we propose minimizing a measure of the horizon, something we call the “subjective discount”, over which rewards need to be optimized to encourage agents to make optimal decisions with less lookahead. To solve this optimization problem, we propose a linear-programming based algorithm that efficiently finds a reward function that maximizes action gap and minimizes subjective discount

Our experiments support three principles of reward design:
1) consistent with existing results, penalizing each step taken induces faster learning than rewarding the goal.
2) When rewarding subgoals along the target trajectory, rewards should gradually increase as the goal gets closer.
3) Dense reward that’s nonzero on every state is only good if designed carefully.
