from encode import encrypt, decrypt

import unittest

tests = [
    ('bond', 'theredfoxtrotsquietlyatmidnight',
     'uvrufrsryherugdxjsgozogpjralhvg'),
    ('train', 'murderontheorientexpress', 'flrlrkfnbuxfrqrgkefckvsa'),
    ('garden', 'themolessnuckintothegardenlastnight',
     'zhvpsyksjqypqiewsgnexdvqkncdwgtixkx'),
]


class TestEncode(unittest.TestCase):
    def test_encrypt(self):
        for t in tests:
            self.assertEqual(encrypt(t[0], t[1]), t[2])

    def test_decrypt(self):
        for t in tests:
            self.assertEqual(decrypt(t[0], t[2]), t[1])
