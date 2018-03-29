from get3sum import get_3sum

import unittest

class Test3Sum(unittest.TestCase):

    def test_sum1(self):
        n = [4, 5, -1, -2, -7, 2, -5, -3, -7, -3, 1]
        r = get_3sum(n)
        self.assertIn((-7, 2, 5), r)
        self.assertIn((-5, 1, 4), r)
        self.assertIn((-3, -2, 5), r)
        self.assertIn((-3, -1, 4), r)
        self.assertIn((-3, 1, 2), r)
        self.assertEqual(5, len(r))

    def test_sum2(self):
        n = [-1, -6, -3, -7, 5, -8, 2, -8, 1]
        r = get_3sum(n)
        self.assertIn((-7, 2, 5), r)
        self.assertIn((-6, 1, 5), r)
        self.assertIn((-3, 1, 2), r)
        self.assertEqual(3, len(r))

    def test_sum3(self):
        n = [-5, -1, -4, 2, 9, -9, -6, -1, -7]
        r = get_3sum(n)
        self.assertIn((-5, -4, 9), r)
        self.assertIn((-1, -1, 2), r)
        self.assertEqual(2, len(r))
