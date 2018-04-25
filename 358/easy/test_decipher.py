from decipher import decipher

import unittest

tests = [
("""    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|""", '123456789'),
("""    _  _  _  _  _  _  _  _ 
|_| _| _||_|| ||_ |_| _||_ 
  | _| _||_||_| _||_||_  _|""", '433805825'),
(""" _  _  _  _  _  _  _  _  _ 
|_  _||_ |_| _|  ||_ | ||_|
 _||_ |_||_| _|  ||_||_||_|""", '526837608'),
(""" _  _        _  _  _  _  _ 
|_||_ |_|  || ||_ |_ |_| _|
 _| _|  |  ||_| _| _| _||_ """, '954105592'),
]


class TestDecipher(unittest.TestCase):
    def test_decipher(self):
        for t in tests:
            self.assertEqual(decipher(t[0]), t[1])
