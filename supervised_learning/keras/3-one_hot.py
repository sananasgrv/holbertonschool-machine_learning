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
        classes = labels.max() + 1
    return K.utils.to_categorical(labels, num_classes=classes)
