import numpy as np
from r_utils import replicate, sample


if __name__ == "__main__":
    n = 100
    n_simulations = 10000
    r = replicate(
        n_simulations,
        lambda: np.sum(sample(n) == np.arange(1, n+1))
    )
    r = np.array(r)
    print(np.sum(r >= 1) / n_simulations)
