#!/usr/bin/python3
"""Unittest function max_integer()
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([10, 20, 30, 40, 50]), 50)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-10, -20, -30, -40, -50]), -10)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 0, 10, -2, 8]), 10)
        self.assertEqual(max_integer([-10, -2, 0, 5, -8]), 5)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 2, 3, 3, 2, 1]), 3)
        self.assertEqual(max_integer([10, 10, 10, 10, 10]), 10)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 4.1]), 4.1)
        self.assertEqual(max_integer([2.3, 5.7, 1.2, 4.9]), 5.7)


if __name__ == '__main__':
    unittest.main()
