import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
minimum_version = ssl.PROTOCOL_TLSv1_2
maximum_version = ssl.PROTOCOL_TLSv1_2
TLSVersion = ssl.PROTOCOL_TLSv1_2

import unittest
from translator import english_to_french, french_to_english


class TestEnglishtofrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertIsNone(english_to_french(None))

class TestFrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNone(french_to_english(None))

if __name__ == '__main__':
    unittest.main()