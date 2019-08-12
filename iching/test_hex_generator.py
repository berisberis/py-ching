import unittest
from iching.hex_generator import Hexagram


class TestTrigram(unittest.TestCase):
    def test_trigram(self):
        first, second, third = Hexagram.trigram()
        # Test the generation of trigrams
        self.assertLessEqual(first, 1, "Must be less than 2")
        self.assertLessEqual(second, 1, "Must be less than 2")
        self.assertLessEqual(third, 1, "Must be less than 2")
        self.assertIsNotNone(Hexagram.trigram())


class TestHexagram(unittest.TestCase):
    def test_hexagram(self):
        hex1, hex2 = Hexagram.create_hexagram()
        assert tuple(hex1)
        assert tuple(hex2)
