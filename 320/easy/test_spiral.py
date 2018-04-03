from spiral import gen_spiral

import unittest


class TestSpiral(unittest.TestCase):
    def get_lengths(self, s):
        return [len(r) for r in s]

    def test_spiral_of_one(self):
        s, w = gen_spiral(1)
        self.assertIn([1], s)
        self.assertEqual(w, 1)

    def test_spiral_of_3(self):
        s, w = gen_spiral(3)
        self.assertEqual(w, 1)
        self.assertEqual(len(s), 3)
        lengths = self.get_lengths(s)
        self.assertEqual(min(lengths), max(lengths))
        self.assertEqual(lengths[0], 3)

    def test_spiral_of_100(self):
        s, w = gen_spiral(10)
        self.assertEqual(w, 3)
        self.assertIn([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], s)
        self.assertIn([32, 61, 82, 95, 100, 99, 90, 73, 48, 15], s)
        lengths = self.get_lengths(s)
        self.assertEqual(min(lengths), max(lengths))
        self.assertEqual(lengths[0], 10)
