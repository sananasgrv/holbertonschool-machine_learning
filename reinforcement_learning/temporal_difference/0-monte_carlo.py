#!/usr/bin/env python3
"""Comment"""
import numpy as np


def monte_carlo(env, V, policy, episodes=5000, max_steps=100,
                alpha=0.1, gamma=0.99):
    """Performs the Monte Carlo algorithm."""

    for episode in range(episodes):
        state, _ = env.reset()

        states = []
        rewards = []

        for step in range(max_steps):
            states.append(state)

            action = policy(state)

            next_state, reward, terminated, truncated, _ = env.step(action)

            rewards.append(reward)
            state = next_state

            if terminated or truncated:
                break

        G = 0

        for t in range(len(states) - 1, -1, -1):
            G = gamma * G + rewards[t]

            state = states[t]

            V[state] = V[state] + alpha * (G - V[state])

    return V
