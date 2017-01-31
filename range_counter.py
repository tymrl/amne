import argparse
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


def read_file(filename):
    with open(filename, encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    n, k = lines[0].split()
    prices = [int(price) for price in lines[1].split()]

    assert int(n) == len(prices), 'n does not equal the number of home values'

    for line in lines[2:]:
        if line:
            raise ValueError('Extra lines detected')

    return RangeCounter(int(n), int(k), prices)


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename',
        help='Name of input file.  Should be UTF-8 encoded (or compatible) and'
             'contain two lines of space-separated integers.'
    )
    parser.add_argument(
        '--matrix',
        help='Use the --matrix flag to print a diagnostic matrix.  Use only '
             'for small examples.',
        action='store_true'
    )

    args = parser.parse_args()
    range_counter = read_file(args.filename)
    range_counter.assign_change_matrix()

    if args.matrix:
        print(range_counter.change_matrix)

    for subrange_sum in range_counter.compute_subrange_sums():
        print(subrange_sum)

run()
