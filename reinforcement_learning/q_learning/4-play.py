#!/usr/bin/env python3
"""Comment"""
import numpy as np


def play(env, Q, max_steps=100):
    """Comment"""

    state = env.reset()[0]
    rendered_outputs = []
    total_rewards = 0

    for step in range(max_steps):
        rendered_outputs.append(env.render())

        action = np.argmax(Q[state])

        new_state, reward, terminated, truncated, _ = env.step(action)

        state = new_state
        total_rewards += reward

        if terminated or truncated:
            rendered_outputs.append(env.render())
            break

    return total_rewards, rendered_outputs
