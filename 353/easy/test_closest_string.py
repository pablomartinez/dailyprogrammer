from closest_string import distance, closest
import unittest


class TestEncode(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(distance('a', 'a'), 0)
        self.assertEqual(distance('a', 'b'), 1)
        self.assertEqual(distance('aa', 'aa'), 0)
        self.assertEqual(distance('xa', 'aa'), 1)
        self.assertEqual(distance('ax', 'aa'), 1)
        self.assertEqual(distance('xx', 'aa'), 2)

    def test_closest(self):
        words = [
            'CTCCATCACAC',
            'AATATCTACAT',
            'ACATTCTCCAT',
            'CCTCCCCACTC',
        ]
        self.assertEqual('AATATCTACAT', closest(words))

    def test_closest_long(self):
        words = [
            'AACACCCTATA',
            'CTTCATCCACA',
            'TTTCAATTTTC',
            'ACAATCAAACC',
            'ATTCTACAACT',
            'ATTCCTTATTC',
            'ACTTCTCTATT',
            'TAAAACTCACC',
            'CTTTTCCCACC',
            'ACCTTTTCTCA',
            'TACCACTACTT',
        ]
        self.assertEqual('ATTCTACAACT', closest(words))

    @unittest.skip
    def test_closest_longest(self):
        words = [
            'ACAAAATCCTATCAAAAACTACCATACCAAT',
            'ACTATACTTCTAATATCATTCATTACACTTT',
            'TTAACTCCCATTATATATTATTAATTTACCC',
            'CCAACATACTAAACTTATTTTTTAACTACCA',
            'TTCTAAACATTACTCCTACACCTACATACCT',
            'ATCATCAATTACCTAATAATTCCCAATTTAT',
            'TCCCTAATCATACCATTTTACACTCAAAAAC',
            'AATTCAAACTTTACACACCCCTCTCATCATC',
            'CTCCATCTTATCATATAATAAACCAAATTTA',
            'AAAAATCCATCATTTTTTAATTCCATTCCTT',
            'CCACTCCAAACACAAAATTATTACAATAACA',
            'ATATTTACTCACACAAACAATTACCATCACA',
            'TTCAAATACAAATCTCAAAATCACCTTATTT',
            'TCCTTTAACAACTTCCCTTATCTATCTATTC',
            'CATCCATCCCAAAACTCTCACACATAACAAC',
            'ATTACTTATACAAAATAACTACTCCCCAATA',
            'TATATTTTAACCACTTACCAAAATCTCTACT',
            'TCTTTTATATCCATAAATCCAACAACTCCTA',
            'CTCTCAAACATATATTTCTATAACTCTTATC',
            'ACAAATAATAAAACATCCATTTCATTCATAA',
            'CACCACCAAACCTTATAATCCCCAACCACAC',
        ]
        self.assertEqual('TTAACTCCCATTATATATTATTAATTTACCC', closest(words))
