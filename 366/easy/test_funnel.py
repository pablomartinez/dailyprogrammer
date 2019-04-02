from funnel import funnel

import unittest

tests = [
  (("leave", "eave"), True),
  (("reset", "rest"), True),
  (("dragoon", "dragon"), True),
  (("eave", "leave"), True),
  (("sleet", "lets"), False),
  (("skiff", "ski"), False)
  ]


class TestInrement(unittest.TestCase):

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
