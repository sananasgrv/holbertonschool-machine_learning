#!/usr/bin/env python3

"""Has the trained agent play an episode of FrozenLake."""

import numpy as np


def play(env, Q, max_steps=100):
    """Has the trained agent play an episode."""

    state, _ = env.reset()
    total_rewards = 0
    rendered_outputs = []

    for step in range(max_steps):
        rendered_outputs.append(env.render())

        action = np.argmax(Q[state])

        new_state, reward, terminated, truncated, _ = env.step(action)

        state = new_state
        total_rewards += reward

        if terminated or truncated:
            break

    # Display the final state
    rendered_outputs.append(env.render())

    return total_rewards, rendered_outputs
