#!/usr/bin/env python3
"""Comment"""
import numpy as np


epsilon_greedy = __import__('2-epsilon_greedy').epsilon_greedy


def sarsa_lambtha(env, Q, lambtha, episodes=5000, max_steps=100,
                  alpha=0.1, gamma=0.99, epsilon=1,
                  min_epsilon=0.1, epsilon_decay=0.05):
    """Performs SARSA(lambda)."""

    for episode in range(episodes):
        state, _ = env.reset()

        eligibility = np.zeros_like(Q)

        action = epsilon_greedy(Q, state, epsilon)

        for step in range(max_steps):
            next_state, reward, terminated, truncated, _ = env.step(action)

            if terminated or truncated:
                td_error = reward - Q[state, action]
            else:
                next_action = epsilon_greedy(Q, next_state, epsilon)
                td_error = (
                    reward
                    + gamma * Q[next_state, next_action]
                    - Q[state, action]
                )

            eligibility[state, action] += 1

            Q += alpha * td_error * eligibility

            eligibility *= gamma * lambtha

            if terminated or truncated:
                break

            state = next_state
            action = next_action

        epsilon = max(
            min_epsilon,
            epsilon * (1 - epsilon_decay)
        )

    return Q
