from all_winners import transitive_winners, lost_against

import unittest


class TestDecipher(unittest.TestCase):

    def test_won_against_villanova(self):
        self.assertEqual(lost_against['Villanova'], ['Butler', "St John's", 'Providence', 'Creighton'])

    def test_decipher(self):
        self.assertEqual(1185, len(transitive_winners('Villanova')))
