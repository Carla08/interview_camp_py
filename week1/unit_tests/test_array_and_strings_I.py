import unittest
from assertpy import assert_that
from week1.arrays_and_strings_I.traverse_array_problems import find_contiguos_to_sort_subarray, \
    move_zeros_to_end, mexican_flag


class TestArrayStrings_I(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_contiguos_to_sort_subarray(self):
        arr = [0, 2, 5, 3, 1, 8, 6, 9]
        expected_start, expected_end = 1, 6
        result_start, result_end = find_contiguos_to_sort_subarray(arr)
        assert_that(expected_start).is_equal_to(result_start)
        assert_that(expected_end).is_equal_to(result_end)

    def test_move_zeros_to_end(self):
        arr = [2, 3, 0, 3, 0, 1, 0]
        expected = [2, 3, 1, 3, 0, 0, 0]
        result = move_zeros_to_end(arr)
        assert_that(result).is_equal_to(expected)

    def test_mexican_flag(self):
        arr = [1, 0, 1, 2, 1, 0, 1, 2]
        mex_flag = mexican_flag(arr)
        assert_that(mex_flag).is_equal_to([0, 0, 1, 1, 1, 1, 2, 2])
