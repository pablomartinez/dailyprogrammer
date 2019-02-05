from additive import persistence

import unittest

tests = [
  [ 13, 1],
  [ 1234, 2],
  [ 9876, 2],
  [ 199, 3],
  [ 99999999999, 3]
  ]


class TestAdditive(unittest.TestCase):
    def test_persistence(self):
        for t in tests:
            self.assertEqual(persistence(t[0]), t[1])
