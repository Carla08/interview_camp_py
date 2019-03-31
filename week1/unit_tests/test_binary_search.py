import unittest
from assertpy import assert_that
from week1.binary_search.binary_search import binary_search, binary_search_duplicates, \
    binary_search_closest

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
