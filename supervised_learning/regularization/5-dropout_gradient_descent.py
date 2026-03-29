#!/usr/bin/env python3
"""Module that updates weights using gradient descent with Dropout."""
import numpy as np


def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """Updates weights of a neural network with Dropout using gradient descent.

    Args:
        Y (numpy.ndarray): one-hot array of shape (classes, m) with correct labels
        weights (dict): dictionary of weights and biases
        cache (dict): dictionary of outputs and dropout masks
        alpha (float): learning rate
        keep_prob (float): probability that a node will be kept
        L (int): number of layers
    """
    m = Y.shape[1]
    dZ = cache['A{}'.format(L)] - Y
    weights_copy = weights.copy()

    for i in range(L, 0, -1):
        A_prev = cache['A{}'.format(i - 1)]
        W = weights_copy['W{}'.format(i)]

        dW = np.matmul(dZ, A_prev.T) / m
        db = np.sum(dZ, axis=1, keepdims=True) / m

        if i > 1:
            dA = np.matmul(W.T, dZ)
            dA *= cache['D{}'.format(i - 1)]
            dA /= keep_prob
            dZ = dA * (1 - cache['A{}'.format(i - 1)] ** 2)

        weights['W{}'.format(i)] -= alpha * dW
        weights['b{}'.format(i)] -= alpha * db
