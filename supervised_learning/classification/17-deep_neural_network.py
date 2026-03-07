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

        for i in layers:
            if not isinstance(i, int) or i <= 0:
                raise TypeError("layers must be a list of positive integers")

        self.L = len(layers)
        self.cache = {}
        self.weights = {}

        for l in range(1, self.L + 1):
            prev_layer_size = nx if l == 1 else layers[l - 2]

            self.weights['W' + str(l)] = np.random.randn(layers[l - 1], prev_layer_size) * \
                                         np.sqrt(2 / prev_layer_size)

            self.weights['b' + str(l)] = np.zeros((layers[l - 1], 1))
