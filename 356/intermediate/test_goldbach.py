from goldbach import goldbach

import unittest

tests = [
        (11, (7, 2, 2)),
        (111, (107, 2, 2)),
        (17, (13, 2, 2)),
        (199, (193, 3, 3)),
        (287, (283, 2, 2)),
        (53, (47, 3, 3))
]

class TestGoldbach(unittest.TestCase):
    def test_goldbach(self):
        for t in tests:
            self.assertIn(t[1], goldbach(t[0]))
