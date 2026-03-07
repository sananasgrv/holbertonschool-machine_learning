#!/usr/bin/env python3
""""Documented"""
import numpy as np


class DeepNeuralNetwork:
    """Documented"""

    def __init__(self, nx, layers):
        """Documented"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if not isinstance(layers, list) or len(layers) < 1:
            raise TypeError("layers must be a list of positive integers")

        if not all(map(lambda x: isinstance(x, int) and x > 0, layers)):
            raise TypeError("layers must be a list of positive integers")

        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        for i in range(1, self.L + 1):
            prev_layer_size = nx if i == 1 else layers[i - 2]

            self.weights['W' + str(i)] = (
                    np.random.randn(layers[i - 1], prev_layer_size) *
                    np.sqrt(2 / prev_layer_size))

            self.weights['b' + str(i)] = np.zeros((layers[i - 1], 1))
