It is a multi-locomotive selection environemnt built with Gymnasium ( OpenAI Gym framework ) for training a Deep Reinforcement Learning agent. It simulates a railway scheduling problem where an agent must optimally assign locomotives to trains.
# DRL
1. NN parameters θ determine the function `f(obs) → action`.
2. NN evaluates observation, producing action vector:
`action = [0.3, 0.8, 0.1, ..., selector_A, selector_B]`
	- These numbers are the “weights assigned to locomotives”
	- They are not NN parameters themselves
3. Environment’s `step(action)` interprets those weights:
	- Maybe uses top-k, softmax, thresholding, or other logic
	- Dispatches locomotives according to these weights, producing the final effect
4. Reward is computed based on what actually happened
5. PPO uses reward to update NN weights θ, so next time it outputs better action weights

# First Version
**Observation Space**
The observation vector has a fixed length of:
`````python
obs_len = len(Station) * 2 * pending_train_information + locomotive_state_information * self.locomotive_count + 2 + 1
``````
- For each of the two stations, we track the next 2 pending trains. Each train is characterized by 3 values
	- `status`: 0.0 = not yet departed, 0.5 = en route, 1.0 = arrived, -1.0 = no train
	- `planned`: normalized time until departure (divided by `OBS_SCALE_TIME`)
	- `dest`: destination station as a float
- A state for every locomotive composed by 3 values:
	- `station`: which station it's currently at
	- `remaining_busy`: how much longer it's occupied 
		- 0 if it is free
	- `distance`: km driven since last maintenance
- One value per station that indicates if there is a train ready to depart and at least 2 locomotives are free at that station.
- Exponential Decay Auxiliar: starts near 1.0 at the beginning and decays toward 0.0 over time. Gives the agent a sense of how far into the episode it is.

The observation space is continuous between -1 and 1.

**Action Space**
It is a continuous space with values between -1 and 1.
It has a fixed length 
- One weight per locomotive remapped to [0,1] 
- One selector element per station for choosing how many locomotive must be sent

**Baseline**
In RL, a baseline is a reference policy you compare your learned agent against. 
A rollout is simply running a policy through the environment from the current state to the end of the episode, collecting rewards along the way.
So a baseline rollout simulation = _"if from this point onward we used the simple/greedy policy instead of the learned agent, how much total reward would we get?"_
The greedy baseline policy:
- Scans for trains ready to depart (departure time reached, not yet departed).
- Checks if at least 2 locomotives are free at the train’s origin.
- Selects up to two trains to different destinations.
- Randomly picks 2 available locomotives per train.
- Sets their action weights to `1.0` (others to `-1.0` → effectively 0 after remapping).
- Sets both selectors to `0.0`, which maps to k = 2 locomotives per train.
If no valid train can be started, it returns a no-op action.

**Reward Function**
It computes the reward at the instant $t$ by taking into account:
- If any train has departed correctly , the agent gets a bonus of $\text{START\_BONUS}$
- If the agent assigns significant weight to locomotives that are currently busy, the agent gets penalized by summing the errors ( weight - 0 = weight ) and scaled by $\text{BUSY\_WEIGHT\_PENALTY}$ 
	- It takes into account the number of locomotives while it was not before.
	- At the beginning it was just the average error.
- If eligible locomotives exist but the agent assigns them all weight 0, the agent gets penalized $\text{PENALTY\_FOR\_ZERO\_WEIGHTS}$
- If the lateness increases or decreases, it gets penalized or a bonus
$$
\text{LATENESS\_WEIGHT} \cdot \text{new\_lateness} - \text{old\_lateness} 
$$
	- Where $\text{LATENESS\_WEIGHT}$ has a negative sign.
- At the end of the episode, if there are never-started trains or a catastrophic scheduling failures happen, the agent gets penalized $\text{MISSED\_PENALTY}$
- Penalize weights assigned to high-mileage locomotives by using a multiplier $\text{DISTANCE\_WEIGHT\_PENALTY}$
$$
\text{DISTANCE\_WEIGHT\_PENALTY} \cdot \sum_{i \in L} \text{w}_i \cdot \frac{\text{distance\_since\_maintenance}}{\text{MAINTENANCE\_KM\_MAX}}
$$



Initial condition: The agent learns quickly and reaches stable positive reward, but it does not beat the greedy baseline and shows instability around step 1500. Entropy collapses steadily and KL is high, indicating aggressive updates and early determinism. Success rate remains noisy and moderate, suggesting reward shaping may dominate over true performance. I would strengthen lateness and missed penalties, reduce PPO learning rate or clip range to lower KL, slightly increase entropy regularization, remove threshold-based reward discontinuities, and ensure reward scaling aligns tightly with operational objectives.

|Trial|learning_rate|clip_range|ent_coef|n_steps|gamma|batch_size|missed|start_bonus|lateness_weight|busy_weight_penalty|penalty_for_zero_weights|min_busy_weight_threshold|idle_ready|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Start Condition|0.0003|0.05|0.001|2048|0.99|64|10|1.5|-0.01|0.1|2|0.1|-1|
|Trial 1|0.00001|0.1|0.003|2048|0.99|64|40|1.2|-0.05|0.05|2|0|0|
|Trial 2|0.00003|0.2|0.003|2048|0.99|64|40|1.2|-0.1|0.0025|2|0|0|


Explanations:
**Trial 1**: The KL divergence is now very low (0.0011 smoothed, ~0.001 range) — the aggressive update problem from the start condition is largely resolved. Entropy loss is declining gently (~12.60 → 12.55) rather than collapsing, which is healthier. But the agent still isn't beating the baseline. Delta Reward (RL - Baseline) sits at a smoothed **-20.923**, meaning the greedy baseline consistently outperforms the agent by ~21 reward units per episode. Delta Lateness is positive on average (~5.86 smoothed), meaning the RL agent is actually producing _more_ lateness than the greedy baseline — which is the core operational failure.
**Trial 2**: shows an agent that is "stable but stuck." While you've fixed the catastrophic entropy collapse and high KL divergence of your initial condition, the agent has converged on a sub-optimal strategy.


# Second Version
My question after performing different trials by changing parameters is:
if the environment is simple and reactive, and greedy is strong,   why doesn’t PPO just learn the greedy behavior and match it?
Our environment is moderately simple.
Greedy is strong.
PPO is solving a noisy, shaped, continuous relaxation of that greedy decision.It converges to a smooth approximation of greedy,   not exact greedy. That yields slightly worse performance.

In this version i try to force PPO to act greedly by removing softmax sampling: it will pick top-k deterministically:
- If PPO suddenly matches greedy: then stochastic sampling is the gap
- If not Then reward shaping or representation is still misaligned.

| Trial   | learning_rate | clip_range | ent_coef | n_steps | gamma | batch_size | missed | start_bonus | lateness_weight | busy_weight_penalty | penalty_for_zero_weights | min_busy_weight_threshold | idle_ready |
| ------- | ------------- | ---------- | -------- | ------- | ----- | ---------- | ------ | ----------- | --------------- | ------------------- | ------------------------ | ------------------------- | ---------- |
| Trial 4 | 0.00003       | 0.2        | 0.001    | 2048    | 0.99  | 64         | 40     | 1.2         | -0.2            | 0.0025              | 2                        | 0                         | 0          |
| Trial 5 | 0.0001        | 0.2        | 0.001    | 2048    | 0.99  | 64         | 40     | 1.2         | -0.2            | 0.0025              | 2                        | 0                         | 0          |

**Trial 4**: the clip_fraction of ~0.0007 is dangerously low. This means almost no policy updates are being clipped — the policy is barely changing. Combined with a still-declining entropy, the agent is slowly collapsing toward a fixed deterministic policy, but not toward a _good_ one. It found a local attractor early and is now converging into it. Even with top-k selection, the network still outputs a continuous weight vector. Greedy assigns exactly the right 2 locomotives with weight 1.0 and ignores the rest. PPO is learning to output weights that _after top-k_ produce acceptable assignments, but the gradient path from "which locomotives got selected" back to "what weights to output" is indirect. The network doesn't receive a clean gradient saying "locomotive 3 was the right choice" — it receives a scalar reward for the whole episode.

**Trial 5**: i increased the learning rate but apart a small improvement, it is still stuck. It seems that the problem is not how the agent chooses the action but how the reward function is built. This trials have been a proof of that.

# Third Version
Sampling actions return back and i changed the reward function:
- I penalize weights assigned to high-mileage locomotives but not linearly as before
$$
\text{DISTANCE\_WEIGHT\_PENALTY} \cdot \sum_{i \in L} \left( \frac{\text{distance\_since\_maintenance}}{\text{MAINTENANCE\_KM\_MAX}}\right)^2
$$
- I changed the penalization on delay
$$
\text{LATENESS\_WEIGHT} \cdot \text{total\_lateness} 
$$

| Trial   | learning_rate | clip_range | ent_coef | n_steps | gamma | batch_size | missed | start_bonus | lateness_weight | busy_weight_penalty | penalty_for_zero_weights | min_busy_weight_threshold | idle_ready |
| ------- | ------------- | ---------- | -------- | ------- | ----- | ---------- | ------ | ----------- | --------------- | ------------------- | ------------------------ | ------------------------- | ---------- |
| Trial 6 | 0.0001        | 0.2        | 0.001    | 2048    | 0.995 | 64         | 20     | 5           | -1              | 0.05                | 2                        | 0                         | 0          |

In our model we are performing an interleaved validation: it is checking the agent's performance every single episode to see if it is improving but the "Evaluation" metrics we see in our graphs are a mix of the agent's performance at different stages of its life. We are looking at a moving target.  
I changed this approach by using an evaluation code ( testing data on ) to strictly evaluate on "new data" that the model hasn't overfitted to, we should use a Disjoint Seed Range.

Average results by using a random data set composed by 100 episodes:

| Trial   | Delta Reward Average| Delta Lateness Average | Delta Success Rate Average |
| ------- | ------------- | ---------- | -------- | 
| Trial 6 |    -26.36     | 0.8      |      -0.6%|  

Delta = ( RL Agent - Baseline ) 

We see that our agent is still stuck because the reward function is highly sparse and punitive while the action space is stochastic : it creates a perfect storm for sub-optimal perfroamcne.
Reward function changes:
- I came back to the original penalization on delay because the new one 
- I introduced a bonus for dispatching a train that was already late
- I introduced a constraint in our reward function
START_BONUS > DISTANCE_PENALTY + BUSY_PENALTY
START_BONUS > DISPATCH_TRAIN_ALREADY_LATE_BONUS
- I removed the penalization for giving non zero weights to unavailable locomotives 
	- If the neural network happens to output a high weight for a busy locomotive, you subtract from the reward. This makes the reward signal very "noisy" because the agent is being penalized for something that didn't actually happen in the environment.
- Introduced a workload balance penalization: If you penalize the "Standard Deviation" of mileage across your fleet at the end of the episode, the agent will learn to rotate locomotives. This reduces the chance that 4 locomotives hit their maintenance limit at the exact same hour (a "Maintenance Spike"), which is where greedy baselines usually fail and cause massive lateness.

| Trial   | learning_rate | clip_range | ent_coef | n_steps | gamma | batch_size | missed | start_bonus | lateness_weight | busy_weight_penalty | penalty_for_zero_weights | min_busy_weight_threshold | idle_ready |
| ------- | ------------- | ---------- | -------- | ------- | ----- | ---------- | ------ | ----------- | --------------- | ------------------- | ------------------------ | ------------------------- | ---------- |
| Trial 7 | 0.0001        | 0.2        | 0.001    | 2048    | 0.995 | 64         | 20     | 5           | -1              | 0.05                | 2                        | 0                         | 0          |

| Trial   | Delta Reward Average| Delta Lateness Average | Delta Success Rate Average |
| ------- | ------------- | ---------- | -------- | 
| Trial 7 |    -4.18     | 0.72      |      -0.7%|  

Before adding new complexity (like proactive maintenance), we should ensure the agent can at least **replicate** the baseline under the same constraints. If the agent can’t match greedy when it has the same "tools," adding more tools will likely just confuse it.
I just allowed a deterministic action selection inside the code during the evaluation.

| Trial   | learning_rate | clip_range | ent_coef | n_steps | gamma | batch_size | missed | start_bonus | lateness_weight | busy_weight_penalty | penalty_for_zero_weights | min_busy_weight_threshold | idle_ready |
| ------- | ------------- | ---------- | -------- | ------- | ----- | ---------- | ------ | ----------- | --------------- | ------------------- | ------------------------ | ------------------------- | ---------- |
| Trial 8 | 0.0001        | 0.2        | 0.001    | 2048    | 0.995 | 64         | 20     | 5           | -2              | 0.005                | 2                        | 0                         | 0          |

| Trial   | Delta Reward Average| Delta Lateness Average | Delta Success Rate Average |
| ------- | ------------- | ---------- | -------- | 
| Trial 8 |    -60.68     | -0.25      |      -0.1%|  

It is first trial where the agent started to learn something: the NN produced different weights for the locomotives and in average it is better than random baseline.
The problem is the entropy:  in a healthy PPO training run, **entropy should generally decrease** over time while it is increasing.
*What is entropy?*
Entropy measures the "randomness" or "uncertainty" of your agent's choices.
- **Decreasing Entropy** (Good): Means the agent is becoming more confident, narrowing its focus onto actions it knows are high-reward.
- **Increasing Entropy** (What you see): Means the agent is becoming _more_ confused or more "spread out" in its decision-making.
I tried to resolve the problem by lowering the *ent_coef* from 0.001 to 0.0001

| Trial   | learning_rate | clip_range | ent_coef | n_steps | gamma | batch_size | missed | start_bonus | lateness_weight | busy_weight_penalty | penalty_for_zero_weights | min_busy_weight_threshold | idle_ready |
| ------- | ------------- | ---------- | -------- | ------- | ----- | ---------- | ------ | ----------- | --------------- | ------------------- | ------------------------ | ------------------------- | ---------- |
| Trial 9 | 0.0001        | 0.2        | 0.0001    | 2048    | 0.995 | 64         | 20     | 5           | -2              | 0.005                | 2                        | 0                         | 0          |

| Trial   | Delta Reward Average| Delta Lateness Average | Delta Success Rate Average |
| ------- | ------------- | ---------- | -------- | 
| Trial 9 |    -19.01     | -0.20     |      +0.3%|  

The entropy is not increasing but it is very unstable: the strategy is to slow down the updates in order that *approx_kl* spikes don+t trigger panic unlearning. I also noticed that the total reward is usually very low ( -1000 or less ) and the idea is to rescale the reward i order to fix the unstable entropy ( the gradients become much more smoother ).
**See Trial 10 on excel.**
N.B. in past experiments parameters value are not so trustable ( i made some mistakes in recording them ).
I rescaled the parameters but the problem was the new added variance penalty ( from 1e-4 to 1e-5here ).
The results are better than before but the entropy loss continues to increase but not too much. The idea is to understand if it will decrease if we increase the number of episodes and increase a little the learning rate.
**See Trial 11 on excel**
I got higher improvements by training for much more episodes ( 10000 ). But looking at the training statistics , i observed that:
- Look at the Entropy graph. It climbed until step 4,000 (exploration) and then began a sharp descent. This means the agent is finally "making up its mind" and committing to specific locomotive selection patterns.
- There is a massive surge in `value_loss` starting at step 4,000. This happens because the agent discovered a new way to get a higher reward (better lateness), and its previous "value predictions" were suddenly wrong.
- The `policy_loss` is dropping sharply but is very noisy. This indicates that while the agent is improving, the updates are quite large.
The fact that it is beating the baseline by 1.32 points of lateness is a clear win. However, the `value_loss` has not yet plateaued, which means the agent hasn't fully mastered its new strategy.
What does it mean?
In reinforcement learning, the Value Loss measures the accuracy of the "Critic." While the "Actor" decides which locomotives to move, the Critic's job is to predict the "Value" (the total expected reward) of being in a certain situation. The Value Loss is essentially the prediction error. If i stop training while the Value Loss is still spiking (as it is at the end of Trial 11), you are saving a model where the internal logic is inconsistent.
**See Trial 12 on excel**
In this trial we found the breaking point ( around the 12k-th episode ): it is called policy collapse or catastrophic forgettin rather than traditional overfitting. This tells us your environment's "sweet spot" for convergence is right around 2,000 to 15,000 episodes.
Our current optimizer is **Ranger21** which is incredibly  powerful but it has a few built-in mechanics that actually fight against PPO's core math:
- PPO is an on-policy algorithm. This means it collects a batch of data using its _exact current brain_ (weights), calculates the advantage, updates those exact weights, and then throws the data away.
- Ranger21 uses a mechanic called **LookAhead**. It maintains two sets of weights: "fast weights" that update normally, and "slow weights" that trail behind. Every few steps, it pulls the fast weights back toward the slow weights.
	- Why this breaks PPO? When LookAhead suddenly pulls our  policy weights backward, the data you just collected in your rollout no longer matches your network. PPO calculates its clipping based on the ratio between the old policy and the new policy. If Ranger21 shifts the weights behind PPO's back, those calculations become garbage, leading to the sudden Policy Collapse we saw at 12k.
I changed to an Adam optimizer which is very standard for the industry with a linear decay: as our model approaches12,000 episodes, our learning rate will be significantly lower. The agent will take smaller, more precise steps, allowing it to "settle" into the bottom of the valley rather than jumping over it.
**See Trial 13 on excel**
I realised that i need also the variance and not just the average for evaluating each trial and i also added a new metric called **Model Win Rate (vs. Baseline)**  and **Model Loose Rate (vs. Baseline)** to express the percentage of how much the model is strictly better than the baseline and how much it is the opposite.
Our entropy is still high ( above 10.0 ) so i increased the ent_coeff to force to explore more during first 10k and i changed the decay of the learning rate: i used the cosine annealing with a warm restart behavior
- We’ll keep the LR flat for 2/3 of the total number of episodes and then let it follow the cosine curve down to a minimum value for the final episodes.
I also tracked new metrics for the probabilities produced by the NN: 
In a continuous PPO agent, the Neural Network doesn't output a single number. It outputs the "recipe" for a Gaussian (Normal) distribution
- mean -> This is the center of the bell curve. It represents the agent's best guess for what the locomotive should do.
- standard deviation -> This is the width of the bell curve. It represents **Uncertainty**. If this is high, the agent is "spraying" actions across a wide range to explore
How to read these graphs:
- They are histograms plotted over time
- The horizontal axis is the value being logged ( mean / std )
- The vertical axis is the time/episodes ( front" line is your most recent episode; the lines "behind" it are previous episodes moving back in time. )
- The height of the peaks represents the density ( The higher a peak is, the more locomotives (or data points) are currently sharing that specific value. )
Reading:
- Actions/Decision_Spread ->  The sharp "teeth" prove the Neural Network has learned specific rules ( if we have only one blob means we have something like a random distribution )
- Actions/Uncertainty_Spread -> A "confused" or exploring agent looks like a tall, flat wall pushed to the right. A "confident" agent looks like sharp, jagged peaks migrating to the left.
	- A flat, uniform "wall" means the agent is in "Mass Exploration" mode. It is treating all 12 locomotives with the exact same level of doubt, applying a "blanket" of randomness to every decision equally.
**See Trial 14 on excel**
The results were worst than before, i increased to much the *ent_coef* and i am rewarding it for being random. I reduce it and i increased the *lateness_weight*. 
**See Trial 15 on excel**
I also addressed one problem: most timesteps are "dead time" where the agent has nothing to do. During these steps, the agent still outputs an action, receives a near-zero reward, and PPO dutifully tries to learn from this noise. Switching to event-based means every sample in your buffer corresponds to a real decision point — a train is ready to depart, locomotives need assigning. Our 2048-step buffer suddenly contains 2048 _meaningful_ decisions instead of maybe 200 meaningful ones and 1848 "just waiting" ones.
In other words: instead of the clock "crawling" forward second-by-second or hour-by-hour, your environment "teleports" through time,only stopping at moments where a decision is actually possible.
I changed the reward function , it gives a basic bonus if you send a train ( *START_BONUS* ) but if the train is on time you get a higher reward ( *ON_TIME_BONUS* ) and i removed the penalization for the distance of each locomotive ( it applies only to the chosen locomotive ).
I also come back to the constant + cosine decay of the learning rate .
**See Trial 16 on excel**
The *value_loss* starts at 30 and only reach 15 aftrér 12k steps ( it is still high ). I rewritten the reward function as a Reward class for centralizing its functioning.
I found a problem with our observation space: If Loco 1 is at Station A and Loco 2 is at Station B, the agent learns a strategy. If you swap them, the observation vector changes entirely, and the agent has to "re-learn" the same logic for the new indices.
I started trying new configuration and this is my Key Design Schema:

**What skill should the agent learn?**
Select correct locomotives for each station and for each trains in order to reduce latency

**What information does the agent need?**
It needs to understand which locomotives ( with their health ) are available per each station and which trains should depart.
Partial observability ( it should not know the whole schedule of the trains , just few ahead ).

**What actions can the agent take?**
It has to select locomotives ( could be discrete or continous with probability )

**How do we measure success?**
The goal metric is the global latency.

After that i changed the *observation space*:
- For each station:
	- Three trains * 2 features (RelativeUrgency, ReadyFlag) -> the agent is interested only in knowing the delta Time ( between the departure and now scaled properly ) and if the train is ready.
- For each potential locomotive: two features (Health, station ,is_available) -> By keeping the locomotives in the list and using `is_available`, we stabilize the weights.  Health is normalized between 0 and 1 :
	- values close to 1 means it has travelled not so much since the last maintenance 
	- values close to 0 means it will need to go to workshop after few km.
- Use a decay factor to allow the agent to be less conservative at the end of the schedule/episode.
I choose to not put the name/id for each locomotive because If we train on a dataset where "Loco B" is always available, the agent will learn to pick "Loco B" simply because of its ID. In the real world, locomotives change states. We want the agent to learn the concept of a "Healthy, available locomotive," not to memorize the names of specific machines.

I changed also the reward function, now it is defined as:
- Penalty when the episode ends
	- A penalty if the workload has not been balanced during the whole episode between episodes
distances = [l.total_distance for l in locomotives]
mean_d = np.mean(distances) + 1e-8 # add small constant to avoid division by zero
self.reward -= VARIANCE_WEIGHT_PENALTY * float(np.var(distances) / (mean_d ))
	- A penalty for each train which has not departed 
- Penalty after each train has departed
	- Penalty relative to the lateness
	- I deleted the penalty about the distance for each locomotive ( useful when the agent will be able to pick locomotives )
	- Reward if a train is departed
	- Bonus Reward if a train is departed on time.

We started simple and then we add complexity Gradually
1. **First**: Get basic movement and goal-reaching working
	1. Be better than the random baseline
2. **Then**: Add obstacles, multiple goals, or time pressure
	1. The agent can start to send locomotive to early maintance
	2. Locomotive may break during the travel
	3. Have more than 2 stations.
3. **Finally**: multi-agent interactions
	1. Use one agent per station ?

With this new configuration , the validation has been done on 500 episodes, the results are still useless.
**See Trial 17 on excel**
Top 10 Feature Importances:
  loco6_available                0.3699
  loco6_health                   0.2184
  loco7_health                   0.0778
  A_train2_ready                 0.0552
  A_train2_urgency               0.0376
  decay                          0.0373
  loco3_health                   0.0345
  B_train1_urgency               0.0336
  loco8_health                   0.0224
  A_train3_urgency               0.0219
Our agent hasn't learned the _concept_ of "assign a healthy, available locomotive to a train." Instead, it has memorized the array index of Loco 6. In a standard Multi-Layer Perceptron (MLP), passing locomotives in a fixed array `[loco1, loco2, ..., locoN]` means the network assigns specific weights to specific array indices. If Loco 6 happens to be a good choice in your training seed, the network hyper-fixates on it. To get the network to understand that locomotives are essentially "clones" with different data, we need to move from a **Global MLP** (which sees a giant flat vector) to a **Shared-Weight MLP** (which sees many small, identical vectors).
I also removed the is_available variable for each locomotive status by using a new mask vector for the observation space.
The `ContinuousActor` then slices this vector into three distinct functional groups:
- Global Features (13 total): Includes demand urgency and "ready" flags for Station A and Station B, plus the temporal decay auxiliary variable.
- Locomotive Mask (10 total): A binary vector where 1.0 indicates a locomotive is free at its station and 0.0indicates it is busy or in maintenance.
- Locomotive Status (20 total): Ten pairs of `[health, station_id]` representing the physical state of the fleet.

The Actor is split into two specialized sub-networks to handle different types of decisions:
- The Shared-Weight MLP (The Locomotive Evaluator):
    - Input (15 features): Concatenates the 13 Global features with the 2 Status features of _one_ specific locomotive.
    - Logic: This network runs 10 times per step (once per locomotive). It learns the "fitness" of a locomotive for the current schedule.
    - Output: Produces 10 individual means (`loc`) and standard deviations (`scale`).
- The Selector MLP (The Station Strategist):
    - Input (13 features): Looks only at the Global features.
    - Logic: Determines the high-level strategy, such as how many locomotives to send from each station (0, 2, or 3).
    - Output: Produces 2 means and 2 scales for the station selectors.
**See Trial 18**
These results are a **massive breakthrough**. Our agent has transitioned from "memorizing array indices" to "understanding operational logic." While the performance delta against the baseline is currently near zero, this is a very positive sign in reinforcement learning called Operational Parity.
Our PPO diagnostic graphs show a very healthy training curve:
- Value Loss: There is a sharp initial drop followed by a very stable floor, meaning your Critic is now accurately predicting rewards.
- Total Loss: The noise is consistent and centered, which is exactly what you want to see in a converging PPO agent.
- Entropy Loss: It is steadily decreasing (becoming more negative), meaning the agent is slowly becoming more confident and less random.
The agent is currently "stuck" at the baseline level because it hasn't found a reason to be _better_ than greedy. To surpass the baseline, it needs to learn Proactive Fleet Management.
- High Uncertainty: Your `Uncertainty_Spread` is still high (~0.7). The agent is still "guessing" between available locomotives rather than picking the one with the best health for the specific trip.
The reason our agent isn't beating the baseline—and why Trial 18/19 shows low KL divergence and zero clipping despite a higher learning rate—is likely because the policy is "lost" in a high-entropy cloud. If our Entropy Loss is **-54**, our agent is essentially a high-performance random number generator. In a continuous space, that much entropy means the "bell curves" (standard deviations) for each locomotive are so wide that the gradient signal from a "good" choice is drowned out by noise.
To move beyond operational parity and start beating the greedy baseline, your `Reward` class needs to incentivize the proactive rotation of the fleet. Even if trips are equal, the goal is to prevent all locomotives from needing maintenance at the same time. I re-introduced the penalization based on the spread of the workload.
Changes:
- Lower the Entropy: Set `ent_coef` to 0.00001 to force the agent to stop being "randomly operational" and start being "intentionally optimal". 
-  Clamp Action Standard Deviation ( between 0.01 and 0.2 )
I executed some tests but the approx_kl and clip_fraction graphs are still strange ( the first one is very low in values and the second one is constantly 0).
In Reinforcement Learning, PPO handles exploration by adding noise (the `scale` / standard deviation) to the network's output to generate a sampled `action`. PPO mathematically assumes that this exact sampled `action` is what caused the reward. But in our code we sampled the action which is not the best ( exploration is handled by PPO´s IndepNormal ) because we are not trusting the agent at all. The environment must trust the agent. We changed the selection logic to be entirely deterministic based on the weights.

The agent started , close to 2000 episodes, to surrender and choose inaction resulting in higher latency ( a difference between baseline and agent over 200 units ). I changed the reward function by penalizing more the latency and increasing the ON_START bonus w.r.t. ON_TIME bonus.
The final result is a better policy but with too many spikes ( it is too good or too bad )
To resolve this I changed my approach and i just introduced a jump off in the epochs iteration if the KL divergency is higher than 0.15 ( in other words: If the policy has moved more than 1.5% away from the old one, stop updating on this batch to prevent a "heavy" crash.)

It did not work out, at some point in the training the lateness just explode.
I added new stats for logging and debugging the model, it seems that it explodes because it understands that is better to not send a train at the end of the episode. This conservative approach seems to give high latency, i tried to put a latency penalization at each departure to be sure that the agent understands the goal ( reduce the latency and leave the system in acceptable state ).

**See Trial 19**

By changing also the value of the MISSED_VALUE it seems that the spikes of the rewards has been corretly avoided.
I tried to change the horizon of the scheduling from 5 to 14 days in order to give much more time to the agent to actually beat the baseline although it is much more complex for him but the result are worst.
I found a bug inside the Neural Network architecture, the global features did not take into account how much locomotives there are in each station.
I changed the observation space by adding two information in the global pool:
- avail_a: number of available locomotives in station A
- avail_b: number of available locomotives in station B
The problem right now is that the training is good bug the evaluation is a mess ( i think it does not focus correctly on understanding the relation between feature of the locomotive and the global information ).
I changed the parameters massively to understand maybe if there is some mismatch between them.
Here a brief description of each parameter:
- learning-rate $\rightarrow$ controls how aggressively the neural network updates its weights after finding a good or bad action.
- ent-coef ( entropy / cuoriosity ) $\rightarrow$ Mathematically forces the agent's action distribution to remain wide, effectively punishing the agent for being "too certain" too early.
	- It is the mathematical force that prevents the agent from becoming too certain too quickly, forcing it to explore different actions.
- clip_range $\rightarrow$ it acts a safety brake for policy updates. If a new strategy is vastly better than the old one, this parameter caps the allowed change to the neural network weights ( it avoids to destroy previous knowledge )
- gamma $\rightarrow$ discount factor gamma controls how much the agent cares about the future versus the present.
- n_envs $\rightarrow$ number of environments running sumultaneously.
- n_step $\rightarrow$ how many steps each parallel environment takes before pausing to update the neural network.
	- In PPO, the Episode and the NN Update (Rollout) are two completely separate timelines that do not have to align.
	![[Screenshot 2026-03-09 at 10.39.02.png]]
- batch_size $\rightarrow$ PPO batch size: once the environments have collected all their steps into a giant memory buffer, the algorithm slices that data into mini-batches of this size to feed through the GPU.
- n_loks $\rightarrow$ number of locomotives available in the simulation
- enable_maintenance $\rightarrow$ When activated, it enforces km-based maintenance, specifically a 12,000 km threshold, 1,500 km per trip, and a 6-hour workshop downtime.
I found a bug due the usage of a wrong parameter: the actual buffer dimension of data was not computed correctly.
I changed the number of scheduled days to 5:
- Number of steps is just 24h \* 5 per day up to the closest number which is a power of 2
- Total Buffer size is just n_envs \* n_steps which is 8 \*256 = 2048 
- Batches is equal to 1024, so exactly half of the buffer size

There was a bug in my project: a mismatch between the representation in the dict of the observation space and how it was handled in my other functions. I resolved the issue.
**See Trial 20**
We did it, it is working: the agent chooses also 3 locomotives and it allows better performance than the random baseline.
The RL model demonstrates strong generalization on the 500 unseen scenarios, showing substantial improvements across all key metrics:
- Reward: The RL Agent achieved a mean reward of 86.29, a +30.75 improvement over the baseline (55.54).
- Lateness: Mean lateness was reduced by nearly 60%, dropping from 68.71 hours to 28.15 hours.
- Success Rate: The agent successfully completed 83.1% of the scenarios, compared to the baseline's 66.8%.
- Head-to-Head: The model is highly reliable, winning 88.8% (444/500) of the trials.
The tree's logic is almost entirely driven by **availability masks**. This confirms that the agent's primary priority is identifying which locomotives are physically capable of being dispatched (i.e., not in maintenance and not busy).

I found a bug: the bug is a critical sequence error in our reinforcement learning environment where the `step` function applies automatic locomotive maintenance immediately before executing the agent's chosen action, violating the Markov Decision Process by allowing the environment to secretly change the state the agent just observed. Because the agent receives an observation that a locomotive is available and outputs an action to use it, but the environment instantly locks that locomotive into maintenance if it crossed the distance threshold, the agent's valid action suddenly fails during the dispatch phase, arbitrarily penalizing the model for a correct choice and destroying the training loop. To completely fix this observation-action misalignment, we must execute the agent's dispatch logic first, advance the simulation clock to the next event, and only then apply environment-driven state changes like scheduled maintenance right before generating the next observation, ensuring the agent's actions always perfectly align with the reality it was shown.