from ducci import ducci
import unittest

class TestDuci(unittest.TestCase):

    def test_ducci(self):
        seq = ducci((1,2,1,2,1,0))
        self.assertEqual(len(seq), 3)

    def test_longer(self):
        seq = ducci((0, 653, 1854, 4063))
        self.assertEqual(len(seq), 24)
