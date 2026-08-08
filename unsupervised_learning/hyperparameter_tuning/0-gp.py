#!/usr/bin/env python3
"""Hyperparameter tuning using Gaussian Processes."""


def __init__(self, X_init, Y_init, l=1, sigma_f=1):
    """Initialize the Gaussian Process.

    Args:
        X_init (numpy.ndarray): The initial input data of shape (t, 1).
        Y_init (numpy.ndarray): The initial output data of shape (t, 1).
        l (float): The length parameter for the kernel.
        sigma_f (float): The standard deviation given to the output of the
            black-box function.
    """
    self.X = X_init
    self.Y = Y_init
    self.l = l
    self.sigma_f = sigma_f
    self.K = self.kernel(X_init, X_init)

    def kernel(self, X1, X2):
        """Compute the kernel matrix between two sets of points.

        Args:
            X1 (numpy.ndarray): The first set of input data of shape (m, 1).
            X2 (numpy.ndarray): The second set of input data of shape (n, 1).

        Returns:
            numpy.ndarray: The kernel matrix of shape (m, n).
        """
        sqdist = np.sum(X1**2, 1).reshape(-1, 1) + np.sum(X2**2, 1) - 2 * np.dot(X1, X2.T)
        return self.sigma_f**2 * np.exp(-0.5 / self.l**2 * sqdist)
    