from funnel2 import find_longest_funnel, load_words, find_funnels
import unittest

class TestMediumFunnel(unittest.TestCase):

    def setUp(self):
        self.words = load_words()

    def test_find_funnels(self):
        self.assertEqual(find_funnels('gnash', self.words), ['gash'])
    
    def test_longest_funnel(self):
        self.assertEqual(find_longest_funnel('gnash', self.words), 4)

    def test_longest_funnel(self):
        self.assertEqual(find_longest_funnel('123455', self.words), 1)

    def test_longest_funnel2(self):
        self.assertEqual(find_longest_funnel('princesses', self.words), 9)
        self.assertEqual(find_longest_funnel('turntables', self.words), 5)
        self.assertEqual(find_longest_funnel('implosive', self.words), 1)
        self.assertEqual(find_longest_funnel('programmer', self.words), 2)

    def test_broken_funnel(self):
        self.assertEqual(find_funnels('1234', self.words), [])