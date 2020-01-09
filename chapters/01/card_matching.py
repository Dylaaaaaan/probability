import numpy as np
from r_utils import replicate, sample


def matching_card_expt(n):
    outcome = sample(n)
    result = np.sum(outcome == np.arange(1, n+1))
    return result


if __name__ == "__main__":
    n = 100
    n_simulations = 10000
    results = replicate(
        n_simulations,
        lambda: matching_card_expt(n)
    )
    results = np.array(results)
    prob_matching_card = np.sum(results >= 1) / n_simulations
    print(f"Probability of matching card = {prob_matching_card}")
