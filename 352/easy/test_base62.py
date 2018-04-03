from base62 import encode62

import unittest


class TestComplexity(unittest.TestCase):
    def test_basic_encode62(self):
        self.assertEqual(encode62(0), '0')
        self.assertEqual(encode62(61), 'Z')
        self.assertEqual(encode62(62), '10')
        self.assertEqual(encode62(62**4), '10000')

    def test_encode62(self):
        self.assertEqual(encode62(187621), 'MO9')
        self.assertEqual(encode62(187622), 'MOa')
        self.assertEqual(encode62(7026425611433322325), '8n36rbfRcDb')
