import unittest
from easy.imgurlinks_352 import *

class TestBaseConversion(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_base62_character(self):
        self.assertEquals("2", get_base62_character(2))
        self.assertEquals("a", get_base62_character(10))
        self.assertEquals("z", get_base62_character(35))
        self.assertEquals("A", get_base62_character(36))
        self.assertEquals("Z", get_base62_character(61))
        self.assertEquals(None, get_base62_character(62))

    def test_find_greatest_exponent_of_n_less_than_m(self):
        self.assertEquals(4, find_greatest_exponent_of_n_loe_than_m(2, 17))
        self.assertEquals(4, find_greatest_exponent_of_n_loe_than_m(2, 16))
        self.assertEquals(3, find_greatest_exponent_of_n_loe_than_m(2, 15))

    def test_convert_from_base10ton(self):
        self.assertEquals("44O", convert_from_base10ton(62, 15674))

    def test_integration(self):
        challenge_path = 'imgurlinks_352_challenge_input.txt'
        expected_output = "MO9\ng62n3\n9b4B\n4Ss\n"

        self.assertEquals(expected_output, generate_output(challenge_path))
