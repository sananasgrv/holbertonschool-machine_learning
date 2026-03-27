#!/usr/bin/env python3
"""Documented"""


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """
    that sets up the gradient descent with
    momentum optimization algorithm in TensorFlow:

    alpha is the learning rate.
    beta1 is the momentum weight.
    Returns: optimizer

    """
    # Update second moment
    s = beta2 * s + (1 - beta2) * np.square(grad)

    # Update variable
    var = var - alpha * grad / (np.sqrt(s) + epsilon)

    return var, s
