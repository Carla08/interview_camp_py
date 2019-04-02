import unittest
from week1.recursion.memoization import x_power_n
from assertpy import assert_that

class TestRecursion(unittest.TestCase):

    def test_x_power_n(self):
        assert_that(x_power_n(2, 11, {})).is_equal_to(2048)