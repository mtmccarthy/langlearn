from typing import Tuple, List, Dict
from functools import reduce
from copy import deepcopy
"""
A solution to Easy Challenge #350
https://www.reddit.com/r/dailyprogrammer/comments/7vm223/20180206_challenge_350_easy_bookshelf_problem/

You have an enormous book collection and want to buy some shelfs. You go to a bookshelfstore and they
sell all kinds of shelfs. The wierd part is, some shelfs are different in length but they all cost the same.

You now want to puzzle your collection so that you can fit as many books on the least number of shelfs

"""


Book = Tuple[int, str]  # (<width>, <title>
BookShelf = Tuple[int, List[Book]]


def parse_input(path: str)-> Tuple[List[Book], List[BookShelf]]:
    input_file = open(path, 'r')
    lines = input_file.readlines()
    input_file.close()

    books = []
    book_shelves = []

    for i, line in enumerate(lines):
        if i == 0:
            book_shelves = parse_bookshelves(line)
        else:
            book = parse_book(line)
            books.append(book)

    return books, book_shelves


def num_books_in_bookshelves(shelves: List[BookShelf]) -> int:
    return _num_books_accum(shelves, 0)


def _num_books_accum(shelves: List[BookShelf], acc: int) -> int:
    if len(shelves) == 0:
        return acc
    else:
        first = shelves[0]
        rest = shelves[1:]
        books_in_first = len(first[1])
        return _num_books_accum(rest, acc + books_in_first)


def parse_bookshelves(line: str) -> List[BookShelf]:
    shelf_lengths = line.split(" ")

    return list(map(lambda length: (int(length), []), shelf_lengths))


def parse_book(line: str):
    length_title = line.split(" ", 1)
    length = int(length_title[0])
    title = length_title[1].rstrip('\n')

    return length, title


def shelves_holding_potential(shelves: List[BookShelf]) -> int:
    if len(shelves) == 0:
        return 0
    else:
        shelve_lengths = list(map(lambda shelf: shelf[0], shelves))
        return reduce(lambda acc, shelf_length: acc + shelf_length, shelve_lengths)


def shelf_has_room(book: Book, shelf: BookShelf) -> bool:
    current_books_held = shelf[1]
    if len(current_books_held) == 0:
        width_current_books = 0
    else:
        width_list = map(lambda book: book[0], current_books_held)
        width_current_books = reduce(lambda acc, next: acc + next, width_list)

    return book[0] + width_current_books <= shelf[0]


def add_book_to_shelf(book: Book, shelf: BookShelf) -> BookShelf:
    #Assumes that shelf_has_room validated adding this book
    book_list_clone = deepcopy(shelf[1])
    book_list_clone.append(book)
    return (shelf[0], book_list_clone)


def valid_shelf_config(books: List[Book], current_shelves: List[BookShelf]) -> bool:
    # Order shelves and books largest to smallest
    ordered_books = sorted(books, reverse=True, key=lambda book: book[0])
    ordered_shelves = sorted(current_shelves, reverse=True, key=lambda shelf: shelf[0])
    largest_book = ordered_books[0]
    largest_shelf = ordered_shelves[0]

    final_shelf_list = []
    visited_books = []
    if largest_book[0] > largest_shelf[0]:
        return False  # No way to store the largest book
    else:
        for shelf in ordered_shelves:
            new_shelf = deepcopy(shelf)
            for book in ordered_books:
                if shelf_has_room(book, new_shelf) and book not in visited_books:
                    new_shelf = add_book_to_shelf(book, new_shelf)
                    visited_books.append(book)

            final_shelf_list.append(new_shelf)

    return num_books_in_bookshelves(final_shelf_list) == len(books)


def is_better_shelf(shelf: BookShelf, current_best: List[BookShelf]) -> bool:
    shelf_is_better_lst = map(lambda next_shelf: shelf[0] > next_shelf[0], current_best)

    return reduce(lambda is_already_better, is_this_better:
                  is_already_better or is_this_better,
                  shelf_is_better_lst
                  )


def replace_smallest_shelf(current_best_shelves: List[BookShelf], new_shelf: BookShelf) -> List[BookShelf]:
    smallest_shelf_index = 0
    new_list = []
    for i, shelf in enumerate(current_best_shelves):
        current_smallest = current_best_shelves[smallest_shelf_index]
        if shelf[0] < current_smallest[0]:
            smallest_shelf_index = i

    for i, shelf in enumerate(current_best_shelves):
        if i == smallest_shelf_index:
            new_list.insert(i, new_shelf)
        else:
            new_list.insert(i, current_best_shelves[i])

    return new_list


def remove_smallest_shelf(shelves: List[BookShelf]) -> List[BookShelf]:
    new_list = []
    current_smallest_index = 0
    for i, shelf in enumerate(shelves):
        current_smallest = shelves[current_smallest_index]
        if shelf[0] < current_smallest[0]:
            current_smallest_index = i

    for i, shelf in enumerate(shelves):
        if not i == current_smallest_index:
            new_list.append(shelf)

    return new_list


def can_remove_smallest_shelf(books: List[Book], shelves: List[BookShelf]) -> bool:
    new_shelves = remove_smallest_shelf(shelves)

    return valid_shelf_config(books, new_shelves)


def optimize_bookshelves(books: List[Book], bookshelves: List[BookShelf]) -> List[BookShelf]:
    current_best_shelves = []
    width_of_all_books = reduce(lambda acc, book: acc + book,
                                map(lambda book: book[0], books))

    shelves = deepcopy(bookshelves)

    while shelves_holding_potential(current_best_shelves) < width_of_all_books:
        current_best_shelves.append(shelves.pop())

    # At this point we have a potential valid shelf list
    while not valid_shelf_config(books, current_best_shelves):
        if len(shelves) == 0:
            return "Impossible"
        else:
            current_best_shelves.append(shelves.pop())

    # Now we definitely have a valid shelf list
    for shelf in shelves:
        # Loop determines if a better shelf list exists
        if is_better_shelf(shelf, current_best_shelves):
            updated_shelves = replace_smallest_shelf(current_best_shelves, shelf)
            if valid_shelf_config(books, updated_shelves):
                current_best_shelves = updated_shelves
        while can_remove_smallest_shelf(books, current_best_shelves): #Remove extra unneeded shelves
            current_best_shelves = remove_smallest_shelf(current_best_shelves)

    return current_best_shelves

def main():
    path = "./easytests/bookshelf350_simple_test_file.txt"
    input_data = parse_input(path)
    books = input_data[0]
    bookshelves = input_data[1]

    new_bookshelves = optimize_bookshelves(books, bookshelves)

if __name__ == '__main__':
    main()