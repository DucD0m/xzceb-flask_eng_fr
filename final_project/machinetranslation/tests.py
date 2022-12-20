import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french(), "You must enter some english text...") #Test for null input

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english(), "You must enter some french text...") #Test for null input

unittest.main()