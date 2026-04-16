#!/usr/bin/env python3
"""Documented"""
from tensorflow import keras as K
inception_block = __import__('0-inception_block').inception_block


def inception_network():
    """Documented"""

    # Input shape (224, 224, 3)
    inputs = K.Input(shape=(224, 224, 3))

    # Stage 1: Initial Convolution and Max Pooling
    x = K.layers.Conv2D(64, (7, 7), strides=(2, 2),
                        padding='same', activation='relu')(inputs)
    x = K.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')(x)

    # Stage 2: Local Response Normalization (skipped in many modern versions,
    # but part of the 2014 paper) and Convolution
    x = K.layers.Conv2D(64, (1, 1), padding='same', activation='relu')(x)
    x = K.layers.Conv2D(192, (3, 3), padding='same', activation='relu')(x)
    x = K.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')(x)

    # Stage 3: Inception 3a and 3b followed by Max Pooling
    x = inception_block(x, [64, 96, 128, 16, 32, 32])  # 3a
    x = inception_block(x, [128, 128, 192, 32, 96, 64])  # 3b
    x = K.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')(x)

    # Stage 4: Inception 4a through 4e followed by Max Pooling
    x = inception_block(x, [192, 96, 208, 16, 48, 64])  # 4a
    x = inception_block(x, [160, 112, 224, 24, 64, 64])  # 4b
    x = inception_block(x, [128, 128, 256, 24, 64, 64])  # 4c
    x = inception_block(x, [112, 144, 288, 32, 64, 64])  # 4d
    x = inception_block(x, [256, 160, 320, 32, 128, 128])  # 4e
    x = K.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')(x)

    # Stage 5: Inception 5a and 5b
    x = inception_block(x, [256, 160, 320, 32, 128, 128])  # 5a
    x = inception_block(x, [384, 192, 384, 48, 128, 128])  # 5b

    # Final Stage: Average Pooling, Dropout, and Softmax
    x = K.layers.AveragePooling2D((7, 7), strides=(1, 1))(x)
    x = K.layers.Dropout(0.4)(x)
    x = K.layers.Dense(1000, activation='softmax')(x)

    model = K.Model(inputs=inputs, outputs=x)

    return model
