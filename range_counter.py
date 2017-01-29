import numpy as np

n = 5
k = 3
prices = [188930, 194123, 201345, 154243, 154243]

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

def compute_subranges(n, k, prices):
    change_matrix = np.array([
        find_change_row(start_point, n, prices) for start_point in range(0, n)
    ])

    for start_point in range(n - k + 1):
        print(int(change_matrix[start_point:start_point + k,
                                start_point:start_point + k].sum()))

compute_subranges(n, k, change_matrix)
