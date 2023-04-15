#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_maxInteger(self):
        """checks the max value
        """
        a = [1, 2, 0, 6, 3]
        self.assertEqual(max_integer(a), 6)
        a = [5]
        self.assertEqual(max_integer(a), 5)
    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)
    def test_floats(self):
        """Test a list of floats."""
        floats = [1.77, 5.45, -7.105, 14.8, 6.0]
        self.assertEqual(max_integer(floats), 14.8)
    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.77, 14.8, -7, 14, 6]
        self.assertEqual(max_integer(ints_and_floats), 14.8)
    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)    
    def test_type(self):
        """make sure type error are raised when necessary
        """
        a = ["hello", 3, "4"]
        self.assertRaises(TypeError, max_integer, a)
        a = 8
        self.assertRaises(TypeError, max_integer, a)
if __name__ == '__main__':
    unittest.main()
