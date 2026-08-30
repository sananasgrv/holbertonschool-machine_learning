#!/usr/bin/env python3

"""Train a DQN agent to play Atari Breakout."""

import gymnasium as gym
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam

from rl.agents import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import EpsGreedyQPolicy


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


env = gym.make("ALE/Breakout-v5")

env = GymnasiumWrapper(env)

nb_actions = env.action_space.n
input_shape = env.observation_space.shape

model = Sequential([
    Conv2D(32, (8, 8), strides=(4, 4), activation="relu",
           input_shape=input_shape),
    Conv2D(64, (4, 4), strides=(2, 2), activation="relu"),
    Conv2D(64, (3, 3), strides=(1, 1), activation="relu"),
    Flatten(),
    Dense(512, activation="relu"),
    Dense(nb_actions, activation="linear")
])

memory = SequentialMemory(limit=1000000, window_length=1)

policy = EpsGreedyQPolicy()

dqn = DQNAgent(
    model=model,
    nb_actions=nb_actions,
    memory=memory,
    policy=policy,
    nb_steps_warmup=50000,
    gamma=0.99,
    target_model_update=10000
)

dqn.compile(Adam(learning_rate=0.00025), metrics=["mae"])

dqn.fit(env, nb_steps=50000, visualize=False, verbose=2)

dqn.save_weights("policy.h5", overwrite=True)

env.close()
