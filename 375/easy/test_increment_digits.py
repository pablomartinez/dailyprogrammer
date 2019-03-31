from increment_digit import increment, numerical_increment

import unittest

tests = [
  [ 123, 234],
  [ 998, 10109],
  [ 19, 210],
  ]


class TestInrement(unittest.TestCase):
    def test_increment(self):
        for t in tests:
            self.assertEqual(increment(t[0]), t[1])

    def test_numerical_increment(self):
        for t in tests:
            self.assertEqual(numerical_increment(t[0]), t[1])
