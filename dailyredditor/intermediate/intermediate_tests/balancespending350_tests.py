import unittest
from intermediate.balancespending350 import *

class TestParseInput(unittest.TestCase):

    def setUp(self):
        self.path = "./350_simple_input.txt"

    def test_parse_input(self):
        self.assertEquals([0, -3, 5, -4, -2, 3, 1, 0],
                          parse_input(self.path))


class TestEquilibriumIndex(unittest.TestCase):

    def setUp(self):
        self.path = "./350_simple_input.txt"
        self.nums = parse_input(self.path)
        self.index_value = generate_index_value(self.nums)
        self.before_sum = generate_before_sum(self.index_value)

    def test_generate_equil_indexes(self):
        self.assertEquals(
            [
                (0, 0, 0, 0),
                (1, -3, 0, 3),
                (2, 5, -3, -2),
                (3, -4, 2, 2),
                (4, -2, -2, 4),
                (5, 3, -4, 1),
                (6, 1, -1, 0),
                (7, 0, 0, 0),
            ],
            calc_equilibrium_indexes(self.nums)
        )

    def test_generate_index_value(self):
        self.assertEquals(
            [
                (0, 0, 0, 0),
                (1, -3, 0, 0),
                (2, 5, 0, 0),
                (3, -4, 0, 0),
                (4, -2, 0, 0),
                (5, 3, 0, 0),
                (6, 1, 0, 0),
                (7, 0, 0, 0),
            ],
            self.index_value
        )

    def test_generate_before_sum(self):
        self.assertEquals(
            [
                (0, 0, 0, 0),
                (1, -3, 0, 0),
                (2, 5, -3, 0),
                (3, -4, 2, 0),
                (4, -2, -2, 0),
                (5, 3, -4, 0),
                (6, 1, -1, 0),
                (7, 0, 0, 0),
            ],
            self.before_sum
        )