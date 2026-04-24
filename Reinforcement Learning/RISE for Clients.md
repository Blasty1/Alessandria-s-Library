Description of the **model v1** to stakeholders:
In the initial version of our system, the environment was completely stable and predictable. The model operated strictly as a highly efficient dispatcher. It evaluated the fleet using a specialized neural network architecture that assessed the operational fitness of each locomotive based on its current station and the distance it had traveled since its last workshop visit. The agent successfully learned to match our baseline operational standards ( e.g. random choose between available locmotives in the correct station withouth considering any attributes ) by identifying which locomotives were physically capable of being dispatched and assigning them to scheduled trains to minimize global lateness. During this phase, maintenance was treated as a rigid rule. A locomotive would only be sent out of service when it hit a hard operational limit, such as exactly 12,000 kilometers of travel. While this proved the model could automate dispatching effectively, it lacked the foresight needed for real-world reliability.

Technical point of view:
- **Neural Network structure**: the breakthrough in this phase was moving from a "Global MLP" to a Shared-Weight MLP. Instead of the agent trying to memorize specific locomotives (e.g., "Loco 6 is always good"), it learned the concept of a healthy locomotive.
	- The Evaluator (Shared-Weight MLP): This sub-network runs 10 times per step (once per locomotive). it looks at the locomotive's Health (distance since maintenance) and Station ID alongside global train demand to produce a "fitness score".
	- The Strategist (Selector MLP): This handles high-level station decisions, such as deciding how many locomotives (0, 2, or 3) to send from a specific station.
- **Continuous Observation space**: the agent could see the urgency and readiness of upcoming trains at two stations ( 3 per each ) , along with the health—defined as the distance since the last maintenance ( 1 means fresh, 0 means it must be sent to maintenance ) —and current location of ten available locomotives
- **Continuous Action Space**: the agent evaluated each locomotive to assign it a continuous fitness weight, while a separate selector network outputted two values to decide exactly how many locomotives to dispatch from each station
- **Reward Function**: the reward function was meticulously structured to prioritize operational punctuality. The agent received positive bonuses for successfully dispatching trains, with additional higher rewards if those trains departed perfectly on time. Conversely, it faced strict penalties for accumulated lateness or entirely missed trains.
**Result**:
- **Trial 22** represents a phenomenal milestone in our model's development and serves as concrete proof that our reinforcement learning agent has successfully learned to outperform the standard greedy baseline. The agent achieved a remarkable 91.2% win rate against the baseline schedule. This means it provided a strictly better operational outcome in the vast majority of our simulated scenarios, while only losing or performing worse in a mere 5.8% of cases. Furthermore, the agent improved the overall success rate of successfully completed train schedules by a very strong 19.1% compared to the baseline's capabilities. From a strict performance standpoint, we saw a massive positive swing in our core metrics. The agent secured an average reward improvement of +34.20 points over the baseline. Most importantly for our real-world operational goals, the agent drastically reduced system lateness, cutting delays by an average of 44.68 units. These numbers conclusively demonstrate that the shared-weight neural network architecture successfully taught the agent how to optimally assign locomotives

![[Screenshot 2026-03-30 at 05.01.49.png]]

![[Screenshot 2026-03-30 at 05.02.28.png]]

![[Screenshot 2026-03-30 at 05.03.00.png]]

Example of episode:
![[Pasted image 20260330051113.png]]
![[Pasted image 20260330051150.png]]
Here we can see how at each step the agent is giving weights/preferences to each locomotive.


Description of the **model v2** to stakeholders:
To make the simulation authentically reflect real-world railway operations, we introduced unexpected mechanical failures into the environment. Rather than allowing the agent to operate in a perfectly predictable world, it must now navigate sudden breakdowns. We implemented this by establishing a predetermined budget of random maintenance events at the start of each simulated schedule. These events are distributed across the timeline to ensure that multiple catastrophic failures do not occur at the exact same moment, forcing the agent to adapt to isolated but highly disruptive operational shocks.

Technical implementation:
- When determining which specific locomotive breaks down, we moved away from purely random selection to a model grounded in real-world physics. We utilize a Weibull probability distribution to calculate mechanical degradation. We specifically configured the mathematical shape parameter to align with the "wear-out" phase of the famous engineering Bathtub Curve. Under this configuration, failure rates are not flat; instead, they increase rapidly and non-linearly as a machine accumulates physical mileage. Consequently, a freshly serviced locomotive has a near-zero chance of failing, while a heavily utilized asset naturally dominates the probability pool when a breakdown event is triggered by the system.
- When the simulation clock strikes a pre-scheduled breakdown time, the system evaluates the real-time health of the active fleet, selects the victim based on the degradation weights, and automatically routes that locomotive into unexpected maintenance. This instantly incurs operational penalties and removes the asset from the agent's control. To ensure the simulation remains stable and does not crash, we built in a crucial safety mechanism: if a breakdown is triggered but zero locomotives are currently idle at the station, the system does not fail. Instead, it intelligently pauses and reschedules the breakdown for a later time when at least one-third of the fleet has returned from their current trips.

This architectural approach offers distinct strategic advantages. By spreading the breakdowns across the entire schedule, we avoid unrealistic clustering, and the degradation-weighted sampling ensures the model accurately punishes the overutilization of specific assets. However, we have also identified key limitations that we are working to address. Because the total number of breakdowns is rigidly fixed at the start of the episode, the environment cannot dynamically increase the breakdown rate even if the agent severely overworks the fleet early on. Furthermore, the timing of the breakdowns is dictated by the simulation clock rather than the actual real-time wear of the fleet, meaning the "when" and the "who" are slightly disconnected. Finally, because the total budget of breakdowns is currently a hardcoded number, it does not automatically scale if we change the fleet size or trip distances, which currently requires manual retuning for different operational scenarios.

**Results**:
- **Trial 25** showed that In terms of overall reliability, the reinforcement learning agent achieved an 81.6% win rate against the baseline schedule. While the loss rate did increase to 17.8%—which is entirely expected given that sudden breakdowns introduce unavoidable chaos that no schedule can perfectly predict—the model still proved to be vastly superior to traditional dispatching logic in the overwhelming majority of cases. Additionally, the agent successfully improved the overall completion rate of train schedules by a solid 13% compared to the baseline's capabilities under the same stressful conditions.
- Looking at the strict operational metrics, the agent secured an average reward improvement of 8.21 points over a baseline reward of 43.71. Most importantly for our actual railway operations, the agent continued to significantly mitigate systemic delays. It successfully cut average lateness by 38.12 units compared to the baseline's lateness of 64.52.

![[Screenshot 2026-03-30 at 05.09.18.png]]

![[Screenshot 2026-03-30 at 05.09.35.png]]

![[Screenshot 2026-03-30 at 05.10.02.png]]

Example of episode:
![[Pasted image 20260330050505.png]]
![[Pasted image 20260330050627.png]]
Here we can see how at each step the agent is giving weights/preferences to each locomotive.
