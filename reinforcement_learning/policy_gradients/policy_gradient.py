#!/usr/bin/env python3
"""Monte-Carlo policy gradient (REINFORCE) utilities."""
import numpy as np


def policy(matrix, weight):
    """Computes the softmax policy for a state matrix and weight.

    matrix is the state (or batch of states)
    weight is the weight matrix
    Returns: the action probabilities for each state
    """
    z = matrix @ weight
    exp = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp / np.sum(exp, axis=1, keepdims=True)


def policy_gradient(state, weight):
    """Computes the Monte-Carlo policy gradient for a state and weight.

    state is a matrix with the current observation of the environment
    weight is the weight matrix
    Returns: the sampled action and the gradient (in that order)
    """
    probs = policy(state.reshape(1, -1), weight)[0]
    action = np.random.choice(len(probs), p=probs)

    one_hot = np.zeros(len(probs))
    one_hot[action] = 1
    grad = state.reshape(-1, 1) @ (one_hot - probs).reshape(1, -1)

    return action, grad
