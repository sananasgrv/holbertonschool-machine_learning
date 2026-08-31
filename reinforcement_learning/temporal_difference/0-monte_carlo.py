#!/usr/bin/env python3
"""Comment"""
import numpy as np


def monte_carlo(env, V, policy, episodes=5000, max_steps=100,
                alpha=0.1, gamma=0.99):
    """Comment"""
    for _ in range(episodes):
        state = env.reset()[0]
        states = [state]
        rewards = []

        for _ in range(max_steps):
            action = policy(state)
            state, reward, terminated, truncated, _ = env.step(action)
            states.append(state)
            rewards.append(reward)
            if terminated or truncated:
                break


        G = 0
        for st, reward in zip(states[:-1][::-1], rewards[::-1]):
            G = gamma * G + reward
            V[st] = V[st] + alpha * (G - V[st])

    return V
