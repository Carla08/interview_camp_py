import unittest
from assertpy import assert_that
from week1.binary_search.binary_search import binary_search, binary_search_duplicates, \
    binary_search_closest, find_min_in_cycled_arr, binary_search_unknown_length

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        element = 2
        index_found = binary_search(arr, element)
        assert_that(index_found).is_equal_to(1)

    def test_binary_search_duplicates(self):
        arr = [1,2,2,2,2,3,4,5,6,7,8,9,10]
        element = 2
        index_found = binary_search_duplicates(arr, element)
        assert_that(index_found).is_equal_to(1)

    def test_binary_search_closest(self):
        arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
        number = 23
        index_closest = binary_search_closest(arr, number)
        assert_that(index_closest).is_equal_to(1)

    def test_find_min_cycled_sorted_arr(self):
        arr = [9,8,7,6,5,1,2]
        index_min = find_min_in_cycled_arr(arr)
        assert_that(index_min).is_equal_to(5)

    def test_binary_search_unknown_end(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        element = 2
        index_found = binary_search_unknown_length(arr, element)
        assert_that(index_found).is_equal_to(1)