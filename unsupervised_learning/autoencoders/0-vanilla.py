#!/usr/bin/env python3
"""Vanilla Autoencoder implementation."""
import tensorflow.keras as keras


def autoencoder(input_dims, hidden_layers, latent_dims):
    """Function that creates a vanilla autoencoder"""
    input_layer = keras.Input(shape=(input_dims,))
    encoder = input_layer

    for layer in hidden_layers:
        encoder = keras.layers.Dense(layer, activation='relu')(encoder)

    latent_space = keras.layers.Dense(latent_dims, activation='relu')(encoder)

    decoder = latent_space
    for layer in reversed(hidden_layers):
        decoder = keras.layers.Dense(layer, activation='relu')(decoder)

    output_layer = keras.layers.Dense(input_dims, activation='sigmoid')(decoder)

    autoencoder_model = keras.Model(inputs=input_layer, outputs=output_layer)
    encoder_model = keras.Model(inputs=input_layer, outputs=latent_space)

    return autoencoder_model, encoder_model
