from nose.tools import eq_
from random import randrange

from range_counter import RangeCounter


def test_basic_example():
    range_counter = RangeCounter(
        5, 3, [188930, 194123, 201345, 154243, 154243]
    )

    range_counter.assign_change_matrix()

    eq_(range_counter.change_matrix.tolist(), [[0, 1, 1,  0, 0],
                                               [0, 0, 1,  0, 0],
                                               [0, 0, 0, -1, 0],
                                               [0, 0, 0,  0, 0],
                                               [0, 0, 0,  0, 0]])

    eq_(range_counter.compute_subrange_sums(), [3, 0, -1])


def test_increasing_example():
    range_counter = RangeCounter(10, 4, range(10))

    range_counter.assign_change_matrix()

    eq_(range_counter.change_matrix.tolist(),
        [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    eq_(range_counter.compute_subrange_sums(), [6] * 7)


def test_degenerate_example():
    range_counter = RangeCounter(1000, 1, [0] * 1000)

    range_counter.assign_change_matrix()

    eq_(range_counter.change_matrix.tolist(), [[0] * 1000] * 1000)
    eq_(range_counter.compute_subrange_sums(), [0] * 1000)


def test_random_example():
    n = 200000
    range_counter = RangeCounter(
        n, randrange(n), [randrange(1000000) for _ in range(n)]
    )

    range_counter.assign_change_matrix()

    for _ in range(10):
        row_index = randrange(n)
        assert set(range_counter.change_matrix[row_index]) in [{0, 1}, {0, -1}]
