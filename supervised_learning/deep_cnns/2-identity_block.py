#!/usr/bin/env python3
"""Documented"""
from tensorflow import keras as K


def identity_block(A_prev, filters):
    """
    Builds an identity block as described in Deep Residual Learning
    for Image Recognition (2015)

    Args:
        A_prev: output from the previous layer
        filters: tuple/list containing (F11, F3, F12)
            F11: number of filters in the first 1x1 convolution
            F3: number of filters in the 3x3 convolution
            F12: number of filters in the second 1x1 convolution

    Returns:
        The activated output of the identity block
    """
    F11, F3, F12 = filters
    initializer = K.initializers.HeNormal(seed=0)

    # Save the input value for the shortcut connection
    A_shortcut = A_prev

    # First component of main path: 1x1 convolution
    x = K.layers.Conv2D(filters=F11, kernel_size=(1, 1), padding='same',
                        kernel_initializer=initializer)(A_prev)
    x = K.layers.BatchNormalization(axis=-1)(x)
    x = K.layers.Activation('relu')(x)

    # Second component of main path: 3x3 convolution
    x = K.layers.Conv2D(filters=F3, kernel_size=(3, 3), padding='same',
                        kernel_initializer=initializer)(x)
    x = K.layers.BatchNormalization(axis=-1)(x)
    x = K.layers.Activation('relu')(x)

    # Third component of main path: 1x1 convolution
    x = K.layers.Conv2D(filters=F12, kernel_size=(1, 1), padding='same',
                        kernel_initializer=initializer)(x)
    x = K.layers.BatchNormalization(axis=-1)(x)

    # Final step: Add shortcut value to main path and pass through ReLU
    x = K.layers.Add()([x, A_shortcut])
    x = K.layers.Activation('relu')(x)

    return x
