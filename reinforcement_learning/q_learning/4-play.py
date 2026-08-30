#!/usr/bin/env python3
"""Has the trained agent play an episode of FrozenLake."""
import numpy as np


def play(env, Q, max_steps=100):
    """Has the trained agent play an episode, always exploiting the Q-table."""
    state = env.reset()[0]
    rendered_outputs = []
    total_rewards = 0

    for step in range(max_steps):
        rendered_outputs.append(env.render())
        action = np.argmax(Q[state])
        new_state, reward, terminated, truncated, info = env.step(action)
        state = new_state
        total_rewards = total_rewards + reward

        if terminated or truncated:
            rendered_outputs.append(env.render())
            break

    return total_rewards, rendered_outputs
