import unittest
from easy.changecalc349 import *


class TestParseInput(unittest.TestCase):

    def setUp(self):
        self.path = "./changecalc349_simple_input.txt"
        self.lines = get_file_lines(self.path)
        self.input_line = get_file_lines(self.path)[0]
        self.output_line = get_file_lines(self.path)[1]
        self.sanitized_input = sanitize_line("[^a-zA-Z:]", self.input_line)
        self.sanitized_output = sanitize_output(self.output_line)

        self.expected_input_line = (10, [5, 5, 2, 2, 1])
        self.expected_output_line = lambda n: n <= 3

    def test_parse_input(self):
        change_coins_lambda = parse_input(self.path)

        self.assertEquals(self.expected_input_line, change_coins_lambda[0])

        func = change_coins_lambda[1]

        for i in range(100):
            self.assertEquals((lambda x: x <= 3)(i), func(i))

    def test_parse_line_to_list_num(self):
        self.assertEquals(self.expected_input_line, parse_line_to_list_num(self.sanitized_input))

    def test_parse_line_to_lambda(self):
        for i in range(100):
            output_function = parse_line_to_lambda(self.sanitized_output)
            self.assertEquals\
                (self.expected_output_line(i), output_function(i))

    def test_sanitize_line(self):
        self.assertEquals("10 5 5 2 2 1", self.sanitized_input)

    def test_sanitize_output(self):
        self.assertEquals("n <= 3", sanitize_output(self.output_line))

class TestCreateChangeAlgorithm(unittest.TestCase):

    def setUp(self):
        self.path = "./changecalc349_simple_input.txt"
        self.lines = get_file_lines(self.path)
        self.input_line = get_file_lines(self.path)[0]
        self.output_line = get_file_lines(self.path)[1]
        self.sanitized_input = sanitize_line("[^a-zA-Z:]", self.input_line)
        self.sanitized_output = sanitize_output(self.output_line)

        self.expected_input_line = (10, [5, 5, 2, 2, 1])
        self.expected_output_line = lambda n: n <= 3
        self.change = self.expected_input_line[0]
        self.coins = self.expected_input_line[1]

    def test_create_change_with_least_coins(self):
        self.assertEquals([5, 5], create_change_with_least_coins(self.change, self.coins))
