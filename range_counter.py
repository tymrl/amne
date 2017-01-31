import argparse
import numpy as np


class RangeCounter:
    """
    A class for holding the calculation of how a list of prices increases and
    decreases.  The primary vehicle for this is the change_matrix, which is
    created row by row.  Further description in _assign_change_row() below.
    """
    def __init__(self, n, k, prices):
        self.n = n
        self.k = k
        self.prices = prices
        self.change_matrix = np.zeros((n, n))

    def _assign_change_row(self, start_point):
        """
        Compute a row of the change_matrix and save it to state.  The row
        associated with a particular start_point is the increasing or
        decreasing subrange starting at start_point and continuing for as long
        as the subrange continues to strictly increase or decrease.  Therefore,
        all rows look like a sequence of 0s, followed by a sequence of 1s or
        -1s (depending on whether the subrange is increasing or decreasing),
        followed by a sequence of zeros.
        """
        # We know our last row is going to be all zeros, so just return that
        # now to make our indices work below
        if start_point == self.n - 1:
            return

        # Figure out whether this subrange is increasing or decreasing
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
        """
        Compute rows of the change matrix for all possible start_points.  This
        yields an upper triangular matrix with zeros on the diagonal.  This
        method MUST be called before compute_subrange_sums().
        """
        for start_point in range(self.n):
            self._assign_change_row(start_point)


    def compute_subrange_sums(self):
        """
        Sum all k x k windows along the diagonal of the change_matrix.  This
        counts all subranges appropriately, and subtracts decreasing subranges
        from increasing ones.  Also convert to integers to avoid numpy types.
        Returns n - k + 1 subrange sums, as that is the number of k x k windows
        in a sequence of n prices.  assign_change_matrix() should be called
        before this function.
        """
        return [
            int(self.change_matrix[start_point:start_point + self.k,
                                   start_point:start_point + self.k].sum())
            for start_point in range(self.n - self.k + 1)
        ]


def read_file(filename):
    """
    Read a file in a specific format and return a RangeCounter object with the
    appropriate parameters.  Does some basic error checking.
    """
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
    """
    Make a CLI for the RangeCounter object.
    """
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


# Actually run our script
if __name__ == '__main__':
    run()
