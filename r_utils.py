"""
Python implementation of R functions.
"""
import numpy as np


def sample(n, k=None):
    """Generates an ordered random sample of k numbers from 1 to n."""
    if k is None:  # return random permutation of 1,2,...,n
        k = n
    rng = np.random.default_rng()
    random_sample = rng.integers(low=1, high=n, endpoint=True, size=k)

    return random_sample


def replicate(n_simulations, expt):
    outcomes = [expt() for _ in range(n_simulations)]

    return outcomes
