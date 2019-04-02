import unittest
from week1.recursion.memoization import x_power_n
from week1.recursion.comb_and_perm import get_combos_length_n
from assertpy import assert_that


class TestRecursion(unittest.TestCase):

    def test_x_power_n(self):
        assert_that(x_power_n(2, 11, {})).is_equal_to(2048)

    def test_print_combos_len_n(self):
        arr = [1, 2, 3, 4, 5]
        expected_combos = [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5],
                           [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]

        for combo in get_combos_length_n(arr, 3):
            assert_that(combo in expected_combos).is_true()
