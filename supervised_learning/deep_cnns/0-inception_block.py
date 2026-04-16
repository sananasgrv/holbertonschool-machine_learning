#!/usr/bin/env python3
"""Documented"""
from tensorflow import keras as K


def inception_block(A_prev, filters):
    """Documented"""
    F1, F3R, F3, F5R, F5, FPP = filters

    # 1. 1x1 Convolution branch
    branch1 = K.layers.Conv2D(filters=F1, kernel_size=(1, 1), padding='same',
                              activation='relu')(A_prev)

    # 2. 1x1 Convolution followed by 3x3 Convolution branch
    branch2 = K.layers.Conv2D(filters=F3R, kernel_size=(1, 1), padding='same',
                              activation='relu')(A_prev)
    branch2 = K.layers.Conv2D(filters=F3, kernel_size=(3, 3), padding='same',
                              activation='relu')(branch2)

    # 3. 1x1 Convolution followed by 5x5 Convolution branch
    branch3 = K.layers.Conv2D(filters=F5R, kernel_size=(1, 1), padding='same',
                              activation='relu')(A_prev)
    branch3 = K.layers.Conv2D(filters=F5, kernel_size=(5, 5), padding='same',
                              activation='relu')(branch3)

    # 4. Max Pooling followed by 1x1 Convolution branch
    # Note: The paper uses a 3x3 max pooling with stride 1 to maintain dimensions
    branch4 = K.layers.MaxPooling2D(pool_size=(3, 3), strides=(1, 1),
                                    padding='same')(A_prev)
    branch4 = K.layers.Conv2D(filters=FPP, kernel_size=(1, 1), padding='same',
                              activation='relu')(branch4)

    # Concatenate all branches along the filter (last) axis
    output = K.layers.Concatenate(axis=-1)([branch1, branch2, branch3, branch4])

    return output
