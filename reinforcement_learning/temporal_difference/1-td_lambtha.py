#!/usr/bin/env python3

"""Comment"""

import numpy as np


def td_lambtha(env, V, policy, lambtha, episodes=5000, max_steps=100,
               alpha=0.1, gamma=0.99):
    """Performs the TD(lambda) algorithm."""

    for episode in range(episodes):
        state, _ = env.reset()

        eligibility = np.zeros_like(V)

        for step in range(max_steps):
            action = policy(state)

            next_state, reward, terminated, truncated, _ = env.step(action)

            if terminated and reward == 0:
                reward = -1

            if terminated or truncated:
                td_error = reward - V[state]
            else:
                td_error = reward + gamma * V[next_state] - V[state]

            eligibility[state] += 1

            V += alpha * td_error * eligibility

            eligibility *= gamma * lambtha

            state = next_state

            if terminated or truncated:
                break

    return V
