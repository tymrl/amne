import numpy as np


def find_change_row(start_point, n, prices):
    change_row = np.zeros(n)
    if start_point == n - 1:
        return change_row
    change = np.sign(prices[start_point + 1] - prices[start_point])
    for end_point in range(start_point + 1, n):
        if np.sign(prices[end_point] - prices[end_point - 1]) == change:
            change_row[end_point] = change
        else:
            break
    return change_row

def compute_subrange_sums(n, k, prices):
    change_matrix = np.array([
        find_change_row(start_point, n, prices) for start_point in range(n)
    ])

    return [
        int(change_matrix[start_point:start_point + k,
                          start_point:start_point + k].sum())
        for start_point in range(n - k + 1)
    ]
