#!/usr/bin/env python3
"""Documented"""
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """
    Sets up Adam optimization for a keras model

    Parameters:
    network: keras model to optimize
    alpha (float): learning rate
    beta1 (float): first Adam parameter
    beta2 (float): second Adam parameter

    Returns:
    None
    """
    if classes is None:
        classes = K.cast(K.reduce_max(labels) + 1, K.int32)

    return K.one_hot(labels, depth=classes)
