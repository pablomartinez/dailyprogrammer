from funnel import funnel, bonus, load_words

import unittest

class TestBasicFunnel(unittest.TestCase):

    def test_simple_start(self):
        self.assertTrue(funnel('leave', 'eave'))

    def test_simple_middle(self):
        self.assertTrue(funnel('reset', 'rest'))

    def test_simple_middle_repeated(self):
        self.assertTrue(funnel('dragoon', 'dragon'))

    def test_simple_wrong_order(self):
        self.assertFalse(funnel('eave', 'leave'))

    def test_simple_reorder(self):
        self.assertFalse(funnel('sleet', 'lets'))

    def test_removing_multiple(self):
        self.assertFalse(funnel('skiff', 'ski'))

class TestBonusFunnel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.words = load_words()

    def test_unknown_word(self):
        self.assertEqual(bonus("affidavit", self.words), [])

    def test_single_word(self):
        self.assertEqual(bonus("dragoon", self.words), ["dragon"])

    def test_multiple_words(self):
        self.assertEqual(set(bonus("boats", self.words)), set(["oats", "bats", "bots", "boas", "boat"]))
