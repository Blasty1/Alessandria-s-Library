import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import gymnasium as gym
from collections import deque
from gymnasium.wrappers import RecordEpisodeStatistics
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')

HID_SIZE = 64

class ModelActor(nn.Module):
    """Actor network - outputs mean action for continuous control"""
    def __init__(self, obs_size, act_size):
        super(ModelActor, self).__init__()
        self.mu = nn.Sequential(
            nn.Linear(obs_size, HID_SIZE),
            nn.Tanh(),
            nn.Linear(HID_SIZE, HID_SIZE),
            nn.Tanh(),
            nn.Linear(HID_SIZE, act_size),
            nn.Tanh(),  # Action bounds: [-1, 1]
        )
        # Log standard deviation for exploration
        self.logstd = nn.Parameter(torch.zeros(act_size))
    
    def forward(self, X):
        return self.mu(X)


class ModelCritic(nn.Module):
    """Critic network - outputs value estimate V(s)"""
    def __init__(self, obs_size):
        super(ModelCritic, self).__init__()
        self.value = nn.Sequential(
            nn.Linear(obs_size, HID_SIZE),
            nn.ReLU(),
            nn.Linear(HID_SIZE, HID_SIZE),
            nn.ReLU(),
            nn.Linear(HID_SIZE, 1),  # Single value output
        )
    
    def forward(self, X):
        return self.value(X)


class AgentA2C:
    """A2C Agent - samples actions from actor network"""
    def __init__(self, actor_net, device="cpu"):
        self.net = actor_net
        self.device = device
    
    def __call__(self, states):
        """
        Sample actions from policy
        
        Args:
            states: numpy array of shape (batch_size, obs_size)
        
        Returns:
            actions: sampled actions with exploration noise
        """
        with torch.no_grad():
            states_v = torch.FloatTensor(states).to(self.device)
            mu_v = self.net(states_v)
            mu = mu_v.data.cpu().numpy()
            logstd = self.net.logstd.data.cpu().numpy()
            
            # Sample actions with Gaussian noise
            rnd = np.random.normal(0, 1, mu.shape)
            actions = mu + np.exp(logstd) * rnd
            actions = np.clip(actions, -1, 1)
            
            return actions


def train_a2c(env_name='LunarLander-v3', num_episodes=200, 
              learning_rate=0.001, gamma=0.99,ent_coeff=0.001,debug = False):
    """
    Train A2C agent on a Gymnasium environment
    
    Args:
        env_name: Gymnasium environment name
        num_episodes: number of episodes to train
        learning_rate: learning rate for both networks
        gamma: discount factor
    """
    
    # Create environment
    env = gym.make(env_name)
    env = RecordEpisodeStatistics(env, buffer_length=num_episodes)
    print(f"Starting training for {num_episodes} episodes...")
    
    obs_size = env.observation_space.shape[0]
    act_size = env.action_space.shape[0]
    
    print(f"\n{'='*60}")
    print(f"Training A2C on {env_name}")
    print(f"Observation size: {obs_size}, Action size: {act_size}")
    print(f"{'='*60}\n")
    
    # Create networks
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    print(f"Using device: {device}\n")
    
    actor = ModelActor(obs_size, act_size).to(device)
    critic = ModelCritic(obs_size).to(device)
    
    # Optimizers
    actor_opt = optim.Adam(actor.parameters(), lr=learning_rate)
    critic_opt = optim.Adam(critic.parameters(), lr=learning_rate)
    
    # Create agent
    agent = AgentA2C(actor, device=device)
    
    # Training loop
    episode_rewards = deque(maxlen=100)
    
    for episode in range(num_episodes):
        # Reset environment
        obs, info = env.reset()
        episode_reward = 0.0
        done = False
        
        states = []
        actions = []
        rewards = []
        values = []
        
        # Collect experience for one episode
        while not done:
            # Get action from agent (add batch dimension)
            action = agent(np.array([obs]))[0]
            
            
            # Take step in environment
            next_obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            
            # Store transition
            states.append(obs)
            actions.append(action)
            rewards.append(reward)
            
            # Get critic's value estimate
            with torch.no_grad():
                obs_v = torch.FloatTensor([obs]).to(device)
                value = critic(obs_v).item()
            values.append(value)
            
            episode_reward += reward
            obs = next_obs
        
        # Compute returns and advantages (backward pass)
        returns = []
        R = 0
        
        for t in reversed(range(len(rewards))):
            R = rewards[t] + gamma * R
            returns.insert(0, R)
        
        # Compute advantages
        advantages = np.array(returns) - np.array(values)
        
        # Convert to tensors for optimization
        states_v = torch.FloatTensor(np.array(states)).to(device)
        actions_v = torch.FloatTensor(np.array(actions)).to(device)
        returns_v = torch.FloatTensor(returns).to(device)
        advantages_v = torch.FloatTensor(advantages).to(device)
        
        # ===== Update Critic =====
        values_pred = critic(states_v).squeeze()
        critic_loss = nn.MSELoss()(values_pred, returns_v)
        
        critic_opt.zero_grad()
        critic_loss.backward()
        critic_opt.step()
        
        # ===== Update Actor =====
        mu_v = actor(states_v)
        logstd_v = actor.logstd
        std_v = torch.exp(logstd_v)
        var_v = std_v.pow(2) # Calculate actual variance

        # Correct Gaussian Log Prob
        log_probs = -0.5 * (((actions_v - mu_v) ** 2 / var_v) + 2 * logstd_v + np.log(2 * np.pi)).sum(dim=1)

        # Entropy of a Gaussian: 0.5 + 0.5 * log(2 * pi * sigma^2)
        dist_entropy = (logstd_v + 0.5 + 0.5 * np.log(2 * np.pi)).mean()

        # Loss with entropy bonus
        actor_loss = -(log_probs * advantages_v).mean() - (ent_coeff * dist_entropy)
        
        actor_opt.zero_grad()
        actor_loss.backward()
        actor_opt.step()
        
        episode_rewards.append(episode_reward)
        
        # Print progress
        if (episode + 1) % 10 == 0:
            avg_reward = np.mean(episode_rewards)
            print(f"Episode {episode + 1:3d}/{num_episodes} | "
                  f"Avg Reward: {avg_reward:7.2f} | "
                  f"Last Reward: {episode_reward:7.2f} | "
                  f"Actor Loss: {actor_loss.item():7.4f} | "
                  f"Critic Loss: {critic_loss.item():7.4f}")
    
    env.close()
    print(f"\n{'='*60}")
    print("Training complete!")
    print(f"{'='*60}\n")
    
    # Print summary statistics
    if debug:
        print(f'\nTraining Summary:')
        print(f'Episode durations: {list(env.time_queue)}')
        print(f'Episode rewards: {list(env.return_queue)}')
        print(f'Episode lengths: {list(env.length_queue)}')

        # Calculate some useful metrics
        avg_reward = np.mean(env.return_queue)
        avg_length = np.mean(env.length_queue)
        std_reward = np.std(env.return_queue)
        
        episode_rewards = list(env.return_queue)
        episodes = range(len(env.return_queue))



        plt.plot(episodes,episode_rewards)
        plt.xlabel('Episode')
        plt.ylabel('Reward')
        plt.title('Learning Curve')
        plt.savefig('learning_curve.png')
        plt.show()
        
        print(f'\nAverage reward: {avg_reward:.2f} ± {std_reward:.2f}')
        print(f'Average episode length: {avg_length:.1f} steps')
        print(f'Success rate: {sum(1 for r in env.return_queue if r > 0) / len(env.return_queue):.1%}')
        
        
    return actor, critic


if __name__ == "__main__":
    # STEP 1: Install dependencies (run in terminal first):
    # pip install gymnasium torch numpy
    
    # STEP 2: Run this script
    print("\n" + "="*60)
    print("A2C Training Script for M1 Mac")
    print("="*60)
    
    # Train on LunarLander-v3
    actor, critic = train_a2c(
        env_name='Pendulum-v1',
        num_episodes=2000,  # Start with 100, increase to 500+ for better results
        learning_rate=0.0002,
        gamma=0.99,
        ent_coeff=0.001,
        debug=True
    )
    
    