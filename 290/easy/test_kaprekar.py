from kaprekar import all_sums, is_kaprekar
import unittest


class TestKaprekar(unittest.TestCase):
    def test_all_sums(self):
        self.assertListEqual(all_sums(5), [5])
        self.assertListEqual(all_sums(12), [3, 12])
        self.assertListEqual(all_sums(345), [39, 48, 345])

    def test_kaprebar(self):
        self.assertTrue(is_kaprekar(9))
        self.assertTrue(is_kaprekar(45))
        self.assertTrue(is_kaprekar(55))
        self.assertTrue(is_kaprekar(99))
        self.assertTrue(is_kaprekar(297))
        self.assertTrue(is_kaprekar(703))
        self.assertTrue(is_kaprekar(999))

    def test_kaprebar_fails(self):
        self.assertFalse(is_kaprekar(3))
        self.assertFalse(is_kaprekar(8))
        self.assertFalse(is_kaprekar(12))
        self.assertFalse(is_kaprekar(44))
        self.assertFalse(is_kaprekar(103))
