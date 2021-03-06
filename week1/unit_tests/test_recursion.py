import unittest
from week1.recursion.memoization import x_power_n
from week1.recursion.comb_and_perm import get_combos_length_n, phone_to_num, \
    get_permutations_length_n, get_all_subsets
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

    def test_phone_to_words(self):
        nums = [2, 5]
        expected_words = ['a', 'j'], ['a', 'k'], ['a', 'l'], ['b', 'j'], ['b', 'k'], ['b', 'l'], \
                         ['c', 'j'], ['c', 'k'], ['c', 'l']
        for word in phone_to_num(nums):
            assert_that(word in expected_words).is_true()

    def test_get_permutations_len_n(self):
        arr = [1, 2, 3]
        expected_permutations = [[1,2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
        for permutation in get_permutations_length_n(arr, 2):
            assert_that(permutation in expected_permutations).is_true()

    def test_get_all_subsets(self):
        arr = [1, 2, 3]
        expected_subsets = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        for subset in get_all_subsets(arr):
            assert_that(subset in expected_subsets).is_true()
