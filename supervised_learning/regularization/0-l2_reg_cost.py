#!/usr/bin/env python3
"""Documented"""
import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """Documented"""
    weight_power = 0
    for i in weights:
        if i.startswith('W'):
            weight_power += np.sum(weights[i] ** 2)
    L2_cost = (lambtha / (2 * m)) * weight_power
    return cost + L2_cost
