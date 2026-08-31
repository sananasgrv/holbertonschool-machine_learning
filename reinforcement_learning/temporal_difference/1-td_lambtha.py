#!/usr/bin/env python3
"""Comment"""
import numpy as np


def td_lambtha(env, V, policy, lambtha, episodes=5000, max_steps=100,
               alpha=0.1, gamma=0.99):
    """Comment"""
    for _ in range(episodes):
        state = env.reset()[0]
        eligibility = np.zeros_like(V)

        for _ in range(max_steps):
            action = policy(state)
            next_state, reward, terminated, truncated, _ = env.step(action)

            # TD error and accumulating eligibility trace for this state.
            delta = reward + gamma * V[next_state] - V[state]
            eligibility[state] += 1

            # Update every state in proportion to its current trace,
            # then decay all traces by gamma * lambda.
            V += alpha * delta * eligibility
            eligibility *= gamma * lambtha

            if terminated or truncated:
                break
            state = next_state

    return V
