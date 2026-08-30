#!/usr/bin/env python3
"""Comment"""
import numpy as np


def q_init(env):
    """Initialize the Q-table with zeros."""

    states = env.observation_space.n
    actions = env.action_space.n

    return np.zeros((states, actions))
