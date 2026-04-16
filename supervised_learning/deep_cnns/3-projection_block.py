#!/usr/bin/env python3
"""Documented"""
from tensorflow import keras as K


def projection_block(A_prev, filters, s=2):
    """
    Builds a projection block as described in Deep Residual Learning
    for Image Recognition (2015)

    Args:
        A_prev: output from the previous layer
        filters: tuple/list containing (F11, F3, F12)
            F11: number of filters in the first 1x1 convolution
            F3: number of filters in the 3x3 convolution
            F12: number of filters in the second 1x1 convolution
        s: stride of the first convolution in both the main path
           and the shortcut connection

    Returns:
        The activated output of the projection block
    """
    F11, F3, F12 = filters
    initializer = K.initializers.HeNormal(seed=0)

    # --- Main Path ---

    # First component: 1x1 convolution with stride s
    x = K.layers.Conv2D(filters=F11, kernel_size=(1, 1), strides=(s, s),
                        padding='same', kernel_initializer=initializer)(A_prev)
    x = K.layers.BatchNormalization(axis=-1)(x)
    x = K.layers.Activation('relu')(x)

    # Second component: 3x3 convolution
    x = K.layers.Conv2D(filters=F3, kernel_size=(3, 3), padding='same',
                        kernel_initializer=initializer)(x)
    x = K.layers.BatchNormalization(axis=-1)(x)
    x = K.layers.Activation('relu')(x)

    # Third component: 1x1 convolution
    x = K.layers.Conv2D(filters=F12, kernel_size=(1, 1), padding='same',
                        kernel_initializer=initializer)(x)
    x = K.layers.BatchNormalization(axis=-1)(x)

    # --- Shortcut Path ---

    # Projection shortcut: 1x1 convolution with stride s to match main path
    shortcut = K.layers.Conv2D(filters=F12, kernel_size=(1, 1), strides=(s, s),
                               padding='same',
                               kernel_initializer=initializer)(A_prev)
    shortcut = K.layers.BatchNormalization(axis=-1)(shortcut)

    # Final step: Add shortcut to main path and apply ReLU
    x = K.layers.Add()([x, shortcut])
    x = K.layers.Activation('relu')(x)

    return x
