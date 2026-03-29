#!/usr/bin/env python3
"""Module that creates a neural network layer with L2 regularization."""
import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """Creates a neural network layer with L2 regularization."""

    regularizer = tf.keras.regularizers.l2(lambtha)
    layer_weight = tf.initializers.VarianceScaling(
        scale=2.0, mode=("fan_avg"))
    output_layer = tf.keras.layers.Dense(
        units=n,
        activation=activation,
        kernel_regularizer=regularizer,
        kernel_initializer=layer_weight
    )(prev)
    return output_layer
