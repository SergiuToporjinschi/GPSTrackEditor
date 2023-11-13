import unittest
from Utilities import TrimmerInterval
import re


class TestParseFilterFunction(unittest.TestCase):

    def test_val_set(self):
        tr = TrimmerInterval(1,5)
        self.assertEqual(tr.val, (1,5))
        pass

    def test_val_get(self):
        tr = TrimmerInterval(1,5)
        tr.val = (0,8)
        self.assertEqual(tr.val, (0,8))
        pass

    def test_constructor_exception(self):
        with self.assertRaises(Exception):
            TrimmerInterval(10,2)
        pass

    def test_set_max_exception(self):
        with self.assertRaises(Exception):
            TrimmerInterval(1,2).max = 0
        pass

    def test_set_min_exception(self):
        with self.assertRaises(Exception):
            TrimmerInterval(1,2).min = 6
        pass

    def test_get_index(self):
        self.assertEqual(TrimmerInterval(1,10).index(0), 0)
        self.assertEqual(TrimmerInterval(1,10).index(5), 5)
        self.assertEqual(TrimmerInterval(1,10).index(9), 9)

        self.assertEqual(TrimmerInterval(2,11).index(0), 1)
        self.assertEqual(TrimmerInterval(2,11).index(5), 6)
        self.assertEqual(TrimmerInterval(2,11).index(9), 10)
        pass

    def test_len(self):
        self.assertEqual(len(TrimmerInterval(0, 9)), 10)
        self.assertEqual(len(TrimmerInterval(0, 2)), 3)
        self.assertEqual(len(TrimmerInterval(1, 3)), 3)

if __name__ == '__main__':
    unittest.main()