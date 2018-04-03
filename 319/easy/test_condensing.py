from condensing import condense_sentence, condense_words

import unittest


class TestComplexity(unittest.TestCase):
    def test_condense_words(self):
        self.assertEqual('liverses', condense_words('live', 'verses'))
        self.assertEqual('uno dos', condense_words('uno', 'dos'))

    def test_condense_sentence(self):
        sentence = "Deep episodes of Deep Space Nine came on the television only after the news."
        self.assertEqual(
            "Deepisodes of Deep Space Nine came on the televisionly after the news.",
            condense_sentence(sentence))
