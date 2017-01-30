import numpy as np


class RangeCounter:
    def __init__(self, n, k, prices):
        self.n = n
        self.k = k
        self.prices = prices
        self.change_matrix = np.zeros((n, n))

    def _assign_change_row(self, start_point):
        if start_point == self.n - 1:
            return
        change = np.sign(
            self.prices[start_point + 1] - self.prices[start_point]
        )
        for end_point in range(start_point + 1, self.n):
            current_change = np.sign(
                self.prices[end_point] - self.prices[end_point - 1]
            )
            if current_change == change:
                self.change_matrix[start_point, end_point] = change
            else:
                break

    def assign_change_matrix(self):
        for start_point in range(self.n):
            self._assign_change_row(start_point)

    def compute_subrange_sums(self):
        return [
            int(self.change_matrix[start_point:start_point + self.k,
                                   start_point:start_point + self.k].sum())
            for start_point in range(self.n - self.k + 1)
        ]
