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

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for i in range(1, self.__L + 1):
            prev_layer_size = nx if i == 1 else layers[i - 2]

            self.__weights['W' + str(i)] = (
                    np.random.randn(layers[i - 1], prev_layer_size) *
                    np.sqrt(2 / prev_layer_size))

            self.__weights['b' + str(i)] = np.zeros((layers[i - 1], 1))

    @property
    def weights(self):
        return self.__weights

    @property
    def cache(self):
        return self.__cache

    @property
    def L(self):
        return self.__L

    def forward_prop(self, X):
        """Documented"""
        self.__cache['A0'] = X

        for l in range(1, self.__L + 1):
            A_prev = self.__cache['A' + str(l - 1)]

            W = self.__weights['W' + str(l)]
            b = self.__weights['b' + str(l)]

            Z = np.dot(W, A_prev) + b

            A_curr = 1 / (1 + np.exp(-Z))

            self.__cache['A' + str(l)] = A_curr

        return self.__cache['A' + str(self.__L)], self.__cache
