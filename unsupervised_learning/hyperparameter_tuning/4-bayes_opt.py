#!/usr/bin/env python3
"""Hyperparameter tuning using Gaussian Processes."""
import numpy as np
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
        self.X_s = np.linspace(bounds[0], bounds[1], ac_samples).reshape(-1, 1)

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
        Z[sigma != 0] = improve[sigma != 0] / sigma[sigma != 0]

        EI = np.zeros_like(mu)
        nonzero = sigma != 0
        EI[nonzero] = improve[nonzero] * norm.cdf(Z[nonzero]) + \
            sigma[nonzero] * norm.pdf(Z[nonzero])

        X_next = self.X_s[np.argmax(EI)]

        return X_next, EI
