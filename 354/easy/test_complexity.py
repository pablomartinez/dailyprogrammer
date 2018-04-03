from complexity import get_decomposition_sum

import unittest


class TestComplexity(unittest.TestCase):
    def test_complexity(self):
        d = get_decomposition_sum(12345)
        self.assertEqual(d, 838)

    def test_more_complexity(self):
        self.assertEqual(7, get_decomposition_sum(12))
        self.assertEqual(43, get_decomposition_sum(456))
        self.assertEqual(4568, get_decomposition_sum(4567))
        self.assertEqual(3491, get_decomposition_sum(345678))

    def test_long(self):
        self.assertEqual(2544788, get_decomposition_sum(1234567891011))
