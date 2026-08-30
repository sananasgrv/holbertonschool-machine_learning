#!/usr/bin/env python3

"""Play Atari Breakout using a trained DQN agent."""

import gymnasium as gym
from tensorflow.keras.models import load_model

from rl.agents import DQNAgent
from rl.policy import GreedyQPolicy
from rl.memory import SequentialMemory


class GymnasiumWrapper(gym.Wrapper):
    """Make Gymnasium compatible with keras-rl2."""

    def reset(self, **kwargs):
        """Reset the environment."""
        result = self.env.reset(**kwargs)
        return result[0] if isinstance(result, tuple) else result

    def step(self, action):
        """Step through the environment."""
        result = self.env.step(action)

        if len(result) == 5:
            observation, reward, terminated, truncated, info = result
            done = terminated or truncated
            return observation, reward, done, info

        return result

    def render(self, **kwargs):
        """Render the environment."""
        return self.env.render()


env = gym.make(
    "ALE/Breakout-v5",
    render_mode="human"
)

env = GymnasiumWrapper(env)

nb_actions = env.action_space.n

model = load_model("policy.h5")

memory = SequentialMemory(limit=100000, window_length=1)

dqn = DQNAgent(
    model=model,
    nb_actions=nb_actions,
    memory=memory,
    policy=GreedyQPolicy()
)

dqn.compile(optimizer="adam")

dqn.load_weights("policy.h5")

dqn.test(env, nb_episodes=1, visualize=True)

env.close()
