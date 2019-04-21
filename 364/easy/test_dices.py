from dices import throw_dices

import unittest
try:
    import unittest.mock as mock
except:
    import mock

def mocked_randint(n, m):
    return m

class TestDices(unittest.TestCase):

    @mock.patch('dices.random.randint', side_effect=mocked_randint)
    def test_simple_dice(self, mock_randint):
        r = throw_dices('1d6')
        self.assertEqual(r, 6)
        mock_randint.assert_called_with(1,6)

    @mock.patch('dices.random.randint', side_effect=mocked_randint)
    def test_multiple_dices(self, mock_randint):
        r = throw_dices('4d10')
        self.assertEqual(r, 40)
        self.assertEqual(mock_randint.call_count, 4)