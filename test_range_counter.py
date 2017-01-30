from nose.tools import eq_

from range_counter import find_change_row, compute_subrange_sums


def test_basic_example():
    n = 5
    k = 3
    prices = [188930, 194123, 201345, 154243, 154243]

    eq_(list(find_change_row(0, n, prices)), [0, 1, 1,  0, 0])
    eq_(list(find_change_row(1, n, prices)), [0, 0, 1,  0, 0])
    eq_(list(find_change_row(2, n, prices)), [0, 0, 0, -1, 0])
    eq_(list(find_change_row(3, n, prices)), [0, 0, 0,  0, 0])
    eq_(list(find_change_row(4, n, prices)), [0, 0, 0,  0, 0])

    eq_(compute_subrange_sums(n, k, prices), [3, 0, -1])
