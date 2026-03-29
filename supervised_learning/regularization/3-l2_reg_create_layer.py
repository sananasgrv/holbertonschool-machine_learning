#!/usr/bin/env python3
"""Module that creates a neural network layer with L2 regularization."""
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """Creates a neural network layer with L2 regularization."""

    layer = tf.keras.layers.Dense(
        units=n,
        activation=activation,
        kernel_regularizer=tf.keras.regularizers.l2(lambtha),
        kernel_initializer='glorot_uniform'
    )

    return layer(prev)
