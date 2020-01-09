import numpy as np
from r_utils import sample, replicate, tabulate


def one_birthday_match_prob(k):
    """Note: This overflows for large k."""
    prob_no_birthday_match = np.prod(
        np.arange(365-k+1, 365+1), dtype=np.float32) / 365**k
    return 1 - prob_no_birthday_match


def birthday_match_expt(k):
    outcome = sample(np.arange(1, 365+1), k, replace=True)
    result = np.max(tabulate(outcome))

    return result


if __name__ == "__main__":
    k = 23  # number of people
    n_simulations = 10000
    results = replicate(
        n_simulations,
        lambda: birthday_match_expt(k)
    )
    results = np.array(results)
    prob_matching_birthday = np.sum(results >= 2) / n_simulations
    print((
        "Probability of matching birthday in a group of "
        f"{k} people is {prob_matching_birthday}"
    ))
