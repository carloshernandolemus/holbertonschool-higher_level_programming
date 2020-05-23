#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Test for max_integer function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([7, 4, -1, 3]), 7)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_repeated_number(self):
        self.assertEqual(max_integer([10, 10, 10]), 10)

    def test_float_numbers(self):
        self.assertEqual(max_integer([12, 15, 18, 11]), 18)

    def test_max_operated_integer(self):
        self.assertEqual(max_integer([-2, -6 * -6, 13]), 36)

    def test_neg_numbers(self):
        self.assertEqual(max_integer([-13, -4, -8, -1]), -1)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, 'Holberton'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (17, 15)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'Num': 1, 'Age': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)
