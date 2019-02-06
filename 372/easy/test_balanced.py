from balanced import balanced,perfect_balanced

import unittest

tests = [
  [ 'xxxyyy', True],
  [ 'yyyxxx', True],
  [ 'xxxyyyy', False],
  [ 'yyxyxxyxxyyyyxxxyxyx', True],
  [ 'xyxxxxyyyxyxxyxxyy', False],
  [ '', True],
  [ 'x', False]
]

perfect_tests = [
  ['aabbxx', True],
  ['xxyya', False],
  [ 'x', True ],
  [ '', True ],
]


class TestBalanced(unittest.TestCase):
    def test_balanced(self):
        for t in tests:
            self.assertEqual(balanced(t[0]), t[1])

    def test_perfect_balanced(self):
        for t in perfect_tests:
            self.assertEqual(perfect_balanced(t[0]), t[1])
