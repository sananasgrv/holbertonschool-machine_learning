#!/usr/bin/env python3
"""Documented"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, learning_rate_decay=False, alpha=0.1,
                decay_rate=1, save_best=False, filepath=None,
                verbose=True, shuffle=False):
    """
    save_best is a boolean indicating whether to save the model after each epoch if it is the best
        a model is considered the best if its validation loss is the lowest that the model has obtained
    filepath is the file path where the model should be saved

    """
    callbacks = []

    if early_stopping and validation_data is not None:
        callbacks.append(K.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=patience
        ))

    if learning_rate_decay and validation_data is not None:
        def schedule(epoch):
            """Inverse time decay schedule."""
            return alpha / (1 + decay_rate * epoch)

        callbacks.append(K.callbacks.LearningRateScheduler(
            schedule,
            verbose=1
        ))

    if save_best and validation_data is not None and filepath is not None:
        callbacks.append(K.callbacks.ModelCheckpoint(
            filepath=filepath,
            monitor='val_loss',
            save_best_only=True
        ))

    return network.fit(
        data,
        labels,
        batch_size=batch_size,
        epochs=epochs,
        verbose=verbose,
        shuffle=shuffle,
        validation_data=validation_data,
        callbacks=callbacks
    )