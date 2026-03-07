#!/usr/bin/env python3
"""Deep Neural Network for multiclass classification"""
import numpy as np
import pickle
import os


class DeepNeuralNetwork:
    """Defines a deep neural network"""

    def __init__(self, nx, layers):
        """class constructor"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        if not all(isinstance(x, int) and x > 0 for x in layers):
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for i in range(1, self.__L + 1):
            prev = nx if i == 1 else layers[i - 2]

            self.__weights["W" + str(i)] = (
                np.random.randn(layers[i - 1], prev) * np.sqrt(2 / prev)
            )

            self.__weights["b" + str(i)] = np.zeros((layers[i - 1], 1))

    @property
    def L(self):
        """number of layers"""
        return self.__L

    @property
    def cache(self):
        """cache dictionary"""
        return self.__cache

    @property
    def weights(self):
        """weights dictionary"""
        return self.__weights

    def forward_prop(self, X):
        """forward propagation"""
        self.__cache["A0"] = X

        for i in range(1, self.__L + 1):

            A_prev = self.__cache["A" + str(i - 1)]
            W = self.__weights["W" + str(i)]
            b = self.__weights["b" + str(i)]

            Z = np.matmul(W, A_prev) + b

            if i == self.__L:
                expZ = np.exp(Z - np.max(Z, axis=0, keepdims=True))
                A = expZ / np.sum(expZ, axis=0, keepdims=True)
            else:
                A = 1 / (1 + np.exp(-Z))

            self.__cache["A" + str(i)] = A

        return A, self.__cache

    def cost(self, Y, A):
        """categorical cross-entropy cost"""
        m = Y.shape[1]
        cost = -np.sum(Y * np.log(A)) / m
        return cost

    def evaluate(self, X, Y):
        """evaluate predictions"""
        A, _ = self.forward_prop(X)
        cost = self.cost(Y, A)

        prediction = np.zeros_like(A)
        prediction[np.argmax(A, axis=0), np.arange(A.shape[1])] = 1

        return prediction, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        """performs gradient descent"""
        m = Y.shape[1]
        A_curr = cache["A" + str(self.__L)]
        dz = A_curr - Y

        for i in range(self.__L, 0, -1):

            A_prev = cache["A" + str(i - 1)]
            W_key = "W" + str(i)
            b_key = "b" + str(i)
            W = self.__weights[W_key]

            dw = np.matmul(dz, A_prev.T) / m
            db = np.sum(dz, axis=1, keepdims=True) / m

            if i > 1:
                dz = np.matmul(W.T, dz) * (A_prev * (1 - A_prev))

            self.__weights[W_key] -= alpha * dw
            self.__weights[b_key] -= alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
        """train the network"""

        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")

        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")

        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")

        if alpha <= 0:
            raise ValueError("alpha must be positive")

        costs = []
        steps = []

        for i in range(iterations + 1):

            A, cache = self.forward_prop(X)
            cost = self.cost(Y, A)

            if i % step == 0 or i == iterations:

                if verbose:
                    print(f"Cost after {i} iterations: {cost}")

                if graph:
                    costs.append(cost)
                    steps.append(i)

            if i < iterations:
                self.gradient_descent(Y, cache, alpha)

        if graph:
            import matplotlib.pyplot as plt
            plt.plot(steps, costs)
            plt.xlabel("iteration")
            plt.ylabel("cost")
            plt.title("Training Cost")
            plt.show()

        return self.evaluate(X, Y)

    def save(self, filename):
        """save model"""
        if not filename.endswith(".pkl"):
            filename += ".pkl"

        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename):
        """load model"""
        if not os.path.exists(filename):
            return None

        with open(filename, "rb") as f:
            return pickle.load(f)
