from nose.tools import eq_, assert_raises
import os
from random import randrange
from tempfile import TemporaryDirectory
from uuid import uuid4

from range_counter import RangeCounter, read_file


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


def test_read_file():
    with TemporaryDirectory() as tempdir:
        # Make sure read_file() runs
        filename = os.path.join(tempdir, '.range%s.txt' % uuid4())

        with open(filename, 'w') as f:
            f.write('4 2\n 111111 22222 33333 444444\n')

        range_counter = read_file(filename)
        range_counter.assign_change_matrix()
        eq_(range_counter.compute_subrange_sums(), [-1, 1, 1])

        # Mismatch between n & number of prices
        with open(filename, 'w') as f:
            f.write('4 2\n 1 2 3')

        with assert_raises(AssertionError):
            range_counter = read_file(filename)

        # Extra lines
        with open(filename, 'w') as f:
            f.write('1\n2\n3\n')

        with assert_raises(ValueError):
            range_counter = read_file(filename)
