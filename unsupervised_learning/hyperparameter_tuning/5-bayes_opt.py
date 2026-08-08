#!/usr/bin/env python3
"""Hyperparameter tuning using Gaussian Processes."""
import numpy as np
from scipy.stats import norm

GP = __import__('2-gp').GaussianProcess


class BayesianOptimization:
    """Bayesian optimization class."""

    def __init__(
            self, f, X_init, Y_init, bounds, ac_samples, l=1,
            sigma_f=1, xsi=0.01, minimize=True):
        """Class constructor"""
        self.f = f
        self.gp = GP(X_init, Y_init, l, sigma_f)
        self.xsi = xsi
        self.minimize = minimize
        self.X_s = np.linspace(
            bounds[0], bounds[1], ac_samples).reshape(-1, 1)

    def acquisition(self):
        """Function that calculates the next best sample location"""
        mu, sigma = self.gp.predict(self.X_s)

        if self.minimize:
            best = np.min(self.gp.Y)
            improve = best - mu - self.xsi
        else:
            best = np.max(self.gp.Y)
            improve = mu - best - self.xsi

        Z = np.zeros_like(mu)
        nonzero = sigma != 0
        Z[nonzero] = improve[nonzero] / sigma[nonzero]

        EI = np.zeros_like(mu)
        EI[nonzero] = (
            improve[nonzero] * norm.cdf(Z[nonzero]) +
            sigma[nonzero] * norm.pdf(Z[nonzero])
        )

        X_next = self.X_s[np.argmax(EI)]

        return X_next, EI

    def optimize(self, iterations=100):
        """Optimizes the black-box function."""
        for _ in range(iterations):
            X_next, _ = self.acquisition()

            # Stop if the proposed point was already sampled
            if np.any(np.isclose(self.gp.X, X_next)):
                break

            # Evaluate the black-box function
            Y_next = self.f(X_next)

            # Update the Gaussian Process
            self.gp.X = np.vstack((self.gp.X, X_next))
            self.gp.Y = np.vstack((self.gp.Y, Y_next))

            # Recompute the GP
            self.gp.K = self.gp.kernel(self.gp.X, self.gp.X)
            self.gp.K_inv = np.linalg.inv(self.gp.K)

        # Return the best sampled point
        if self.minimize:
            index = np.argmin(self.gp.Y)
        else:
            index = np.argmax(self.gp.Y)

        X_opt = self.gp.X[index]
        Y_opt = self.gp.Y[index]

        return X_opt, Y_opt
