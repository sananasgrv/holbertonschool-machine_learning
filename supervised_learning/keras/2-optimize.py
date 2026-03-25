#!/usr/bin/env python3
"""Documented"""
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """
    The last dimension of the one-hot matrix must be the number of classes
    Returns: the one-hot matrix
    """

    if not isinstance(labels, np.ndarray):
        return None

        # Flatten in case labels are not 1D
    labels = labels.flatten()

    # Determine number of classes if not provided
    if classes is None:
        classes = np.max(labels) + 1

    m = labels.shape[0]

    # Create one-hot matrix
    one_hot_matrix = np.zeros((m, classes))
    one_hot_matrix[np.arange(m), labels] = 1

    return one_hot_matrix
