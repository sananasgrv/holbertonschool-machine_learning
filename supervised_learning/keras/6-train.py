#!/usr/bin/env python3
"""Documented"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, verbose=True, shuffle=False):
    """
    early_stopping is a boolean that indicates whether
    early stopping should be used

    early stopping should only be performed if validation_data exists
    early stopping should be based on validation loss

    patience is the patience used for early stopping
    """
    callbacks = []

    if early_stopping and validation_data is not None:
        callbacks.append(K.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=patience
        ))

    return network.fit(
        data,
        labels,
        batch_size=batch_size,
        epochs=epochs,
        validation_data=validation_data,
        verbose=verbose,
        shuffle=shuffle,
        callbacks=callbacks
    )
