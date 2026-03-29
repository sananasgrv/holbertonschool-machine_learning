#!/usr/bin/env python3
"""Documented"""
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """Documented"""

    layer = tf.keras.layer.Dense(
        units=n,
        activation=activation,
        kernel_regularizer = tf.keras.regularizers.l2(lambtha)(prev)
    )
    return layer
