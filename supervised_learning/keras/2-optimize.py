#!/usr/bin/env python3
"""Documented"""
import tensorflow.keras as K

def optimize_model(network, alpha, beta1, beta2):
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

    optimizer = K.optimizers.Adam(
        learning_rate=alpha,
        beta_1=beta1,
        beta_2=beta2
    )

    network.compile(
        optimizer=optimizer,
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
