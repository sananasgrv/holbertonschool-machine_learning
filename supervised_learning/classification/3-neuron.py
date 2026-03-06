#!/usr/bin/env python3
""""Documented"""
import numpy as np


class Neuron:
    """Neuron"""

    def __init__(self, nx, b=0, A=0):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Documented"""
        return self.__W

    @property
    def b(self):
        """Documented"""
        return self.__b

    @property
    def A(self):
        """Documented"""
        return self.__A

    def forward_prop(self, X):
        """Documented"""
        Z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """Documented"""
        result = -np.sum(Y * np.log(A) + (1 - Y)
                         * np.log(1.0000001 - A)) / Y.shape[1]
        return result

    def evaluate(self, X, Y):
        """Documented"""
