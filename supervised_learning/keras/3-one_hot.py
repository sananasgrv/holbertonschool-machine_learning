#!/usr/bin/env python3
"""Documented"""
import tensorflow as tf


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
        classes = tf.cast(tf.reduce_max(labels) + 1, tf.int32)

    return tf.one_hot(labels, depth=classes)
