#!/usr/bin/env python3
"""Comment"""
import numpy as np


def q_init(env):
    """Comment"""
    states = env.observation_space.n
    actions = env.action_sapce.n
    return np.zeros((states, actions))
