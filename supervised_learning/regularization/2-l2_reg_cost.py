#!/usr/bin/env python3
"""Documented"""
import tensorflow as tf


def l2_reg_cost(cost, model):
    """Documented"""

    total_costs = [cost + loss for loss in model.losses]
    return total_costs
