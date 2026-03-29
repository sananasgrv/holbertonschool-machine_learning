#!/usr/bin/env python3
"""Module that creates a neural network layer using dropout."""
import tensorflow as tf


def dropout_create_layer(prev, n, activation, keep_prob, training=True):
    """Creates a layer of a neural network using dropout."""

    dense = tf.keras.layers.Dense(
        units=n,
        activation=activation,
        kernel_initializer='glorot_uniform'
    )(prev)

    dropout = tf.keras.layers.Dropout(rate=1 - keep_prob)

    return dropout(dense, training=training)
