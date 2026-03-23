#!/usr/bin/env python3
"""Documented"""
import tensorflow as tf


def l2_reg_cost(cost, model):
    """Documented"""

    total_cost = cost + tf.add_n(model.losses)

    return total_cost
