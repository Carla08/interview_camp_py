import unittest
from assertpy import assert_that
from week1.arrays_and_strings_I.traverse_array_problems import find_contiguos_to_sort_subarray

class TestArrayStrings_I(unittest.TestCase):
    def setUp(self):
        pass

    def test_find_contiguos_to_sort_subarray(self):
        arr = [0,2,5,3,1,8,6,9]
        expected_start, expected_end = 1,6
        result_start, result_end = find_contiguos_to_sort_subarray(arr)
        assert_that(expected_start).is_equal_to(result_start)
        assert_that(expected_end).is_equal_to(result_end)
