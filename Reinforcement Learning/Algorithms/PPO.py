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
              learning_rate_actor=1e-5,
              learning_rate_critic=1e-4,
              gamma=0.99,
              GAE_lambda=0.001,
              eps = 0.2,
              epoches = 10,
              batch_size = 64
              debug = False):
    """
    Train A2C agent on a Gymnasium environment
    
    Args:
        env_name: Gymnasium environment name
        num_episodes: number of episodes to train
        learning_rate: learning rate for both networks
        gamma: discount factor
    """
    