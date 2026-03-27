#!/usr/bin/env python3
"""Documented"""


def update_variables_momentum(alpha, beta1, var, grad, v):
    """
    that updates a variable using the gradient descent
    with momentum optimization algorithm:

    alpha is the learning rate
    beta1 is the momentum weight
    var is a numpy.ndarray containing the variable to be updated
    grad is a numpy.ndarray containing the gradient of var
    v is the previous first moment of var
    Returns: the updated variable and the new moment, respectively
    """
    v_new = beta1 * v + (1 - beta1) * grad

    var_updated = var - alpha * v_new

    return var_updated, v_new