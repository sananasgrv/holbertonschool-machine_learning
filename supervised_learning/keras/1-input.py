#!/usr/bin/env python3
"""Documented"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    Documented
    """

    # First layer (this creates the input tensor implicitly)
    x = K.layers.Dense(
        layers[0],
        activation=activations[0],
        kernel_regularizer=K.regularizers.l2(lambtha),
        input_shape=(nx,)
    )()

    # Keep reference to input
    inputs = x._keras_history.layer.input

    # Hidden layers
    for i in range(1, len(layers)):
        # Apply dropout before each new layer
        x = K.layers.Dropout(1 - keep_prob)(x)

        x = K.layers.Dense(
            layers[i],
            activation=activations[i],
            kernel_regularizer=K.regularizers.l2(lambtha)
        )(x)

    # Build model
    model = K.Model(inputs=inputs, outputs=x)

    return model
