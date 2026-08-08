#!/usr/bin/env python3
"""Vanilla Autoencoder implementation."""
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense


def autoencoder(input_dims, hidden_layers, latent_dims):
    """Function that creates a vanilla autoencoder"""
    input_layer = Input(shape=(input_dims,))
    x = input_layer

    for units in hidden_layers:
        x = Dense(units, activation='relu')(x)

    latent_layer = Dense(latent_dims, activation='relu')(x)

    x = latent_layer
    for units in reversed(hidden_layers):
        x = Dense(units, activation='relu')(x)

    output_layer = Dense(input_dims, activation='sigmoid')(x)

    autoencoder_model = Model(inputs=input_layer, outputs=output_layer)
    encoder_model = Model(inputs=input_layer, outputs=latent_layer)

    return autoencoder_model, encoder_model
