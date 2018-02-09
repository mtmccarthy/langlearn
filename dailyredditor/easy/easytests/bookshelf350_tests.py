import unittest
from easy.bookshelf350 import *


class TestParseInput(unittest.TestCase):

    def setUp(self):
        pass

    def test_parse_bookshelves(self):
        test_line = "500 500 230 4300"
        expected_lst = [
            (500, []),
            (500, []),
            (230, []),
            (4300, [])
        ]

        self.assertEquals(expected_lst, parse_bookshelves(test_line))

    def test_parse_book(self):
        test_line = "70 A Game of Thrones"
        expect = (70, "A Game of Thrones")

        self.assertEquals(expect, parse_book(test_line))

    def test_integration(self):
        path = "./bookshelf350_simple_test_file.txt"
        expectedBookshelf = [
            (150, []),
            (150, []),
            (300, []),
            (150, []),
            (150, [])
        ]
        expectedBooks = [
            (70, "A Game of Thrones"),
            (76, "A Clash of Kings"),
            (99, "A Storm of Swords"),
            (75, "A Feasts for Crows"),
            (105, "A Dance With Dragons")
        ]

        self.assertEquals((expectedBooks, expectedBookshelf),
                          parse_input(path))


class TestOptimizeBookshelves(unittest.TestCase):
    def setUp(self):
        self.path = "./bookshelf350_simple_test_file.txt"
        self.input_data = parse_input(self.path)
        self.books = self.input_data[0]
        self.bookshelves = self.input_data[1]
        self.sample_shelves = [
            (70, [(5, ""), (10, ""), (15, ""), (10, ""), (15, "")]),
            (71, [(7, ""), (11, ""), (22, "")]),
            (72, [(0, ""), (70, "")]),
            (73, [(68, ""), (10, ""), (15, "")])
        ]

    def test_num_books_in_bookshelves(self):
        empty_shelf = (70, [])
        empty_shelves = [empty_shelf] * 5
        self.assertEquals(0, num_books_in_bookshelves(empty_shelves))

        self.assertEquals(13, num_books_in_bookshelves(self.sample_shelves))

    def test_replace_smallest_shelf(self):
        smallest_shelf = self.sample_shelves[0]
        self.assertEquals(70, smallest_shelf[0])
        replace_shelf = (55, [])
        self.assertEquals(replace_shelf, replace_smallest_shelf(self.sample_shelves, replace_shelf)[0])

    def test_remove_smallest(self):
        smallest_shelf = self.sample_shelves[0]
        self.assertEquals(70, smallest_shelf[0])
        self.assertNotEqual(smallest_shelf, remove_smallest_shelf(self.sample_shelves)[0])

    def test_minimum_bookshelves_required_simple(self):
        self.assertEquals(2, len(optimize_bookshelves(self.books, self.bookshelves)))

    def test_shelves_holding_potential(self):
        self.assertEquals(286, shelves_holding_potential(self.sample_shelves))

    def test_is_better_shelf(self):
        worse_shelf = (3, [])
        self.assertFalse(is_better_shelf(worse_shelf, self.sample_shelves))
        better_shelf = (100, [])
        self.assertTrue(is_better_shelf(better_shelf, self.sample_shelves))

    def test_valid_shelf_config(self):
        pass

    def test_shelf_has_room(self):
        shelf = (6, [(1, ""), (3, "")])
        self.assertTrue(shelf_has_room((2, ""), shelf))
        self.assertTrue(shelf_has_room((1, ""), shelf))
        self.assertFalse(shelf_has_room((3, ""), shelf))

    def test_add_book_to_shelf(self):
        shelf = (6, [(1, ""), (3, "")])
        book_to_add = (2, "")
        expected_shelf = (6, [(1, ""), (3, ""), (2, "")])
        self.assertEquals(expected_shelf, add_book_to_shelf(book_to_add, shelf))
