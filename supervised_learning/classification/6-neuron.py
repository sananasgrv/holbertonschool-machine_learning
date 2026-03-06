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
        result = -np.sum(Y * np.log(A) +
                         (1 - Y) * np.log(1.0000001 - A)) / Y.shape[1]
        return result

    def evaluate(self, X, Y):
        """Documented"""
        A = self.forward_prop(X)
        predict = np.where(A >= 0.5, 1, 0).astype(int)
        cost = self.cost(Y, A)
        return predict, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Documented"""
        m = X.shape[1]
        Z = A - Y
        dW = (1 / m) * np.dot(X, Z.T)
        db = (1 / m) * np.sum(Z)
        self.__W = self.__W - alpha * dW.T
        self.__b = self.__b - alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """Documented"""
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be an float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")

        for i in range(iterations):
            self.forward_prop(X)
            self.gradient_descent(X, Y, alpha)

        return self.evaluate(X, Y)
