from typing import Tuple, List, Callable, Dict
import re
import functools
import itertools

"""
Solution to easy challenge #349 Change Calculator

You own a nice tiny mini-market that sells candies to children. You need to know if you'll be able to give the change back to those little cute creatures and it happens you don't know basic math because when you were a child you were always eating candies and did not study very well. So you need some help from a little tool that tell you if you can.

On the line beginning "Input:" be given a single number that tells you how much change to produce, and then a list of coins you own. The next line, beginning with "Output:", tells you the number of coins to give back to achieve the change you need to give back (bounded by the number of coins you have). Here's one that says "give the customer 3 or fewer coins". Example:

Input: 10 5 5 2 2 1
Output: n <= 3

Your progam should emit the coins you would give back to yield the correct value of change, if possible. Multiple solutions may be possible. If no solution is possible, state that. Example:

5 5

"""

def sanitize_output(line: str) -> str:
    return line[8:] # Remove leading Output line

def get_file_lines(path: str) -> List[str]:
    input_file = open(path)
    lines = input_file.readlines()
    input_file.close()

    return lines


def parse_input(path: str) -> Tuple[List[int], Callable[[int], List[int]]]:

    lines = get_file_lines(path)

    _input_line = lines[0]
    _output_line = lines[1]

    input_line = sanitize_line("[^a-zA-Z:]", _input_line)
    output_line = sanitize_output(_output_line)

    return parse_line_to_list_num(input_line), parse_line_to_lambda(output_line)


def sanitize_line(chars_to_keep_regex: str, line: str):
    new_string = ""
    for char in line:
        match = re.search(chars_to_keep_regex, char)
        if match:
            new_string += char

    return new_string.strip()


def parse_line_to_list_num(input_line: str) -> Tuple[int, List[int]]:
    str_nums = input_line.split(" ")
    int_nums = list(map(lambda num: int(num), str_nums))

    change = int_nums[0]
    coins = int_nums[1:]

    return change, coins


def parse_line_to_lambda(input_line: str) -> Callable[[int], List[int]]:
    divisor_str = re.search(r'\d', input_line).group()
    divisor = int(divisor_str)
    divisor_length = len(divisor_str)
    line_length = len(input_line)


    # The idea here is to find all the characters between the variable i.e. n and the comparative
    # int. Then we strip the extra spaces and we have the string equivalent of the operator
    operator = input_line[1:(line_length - divisor_length)].strip()

    return functools.partial(lambda var: eval(str(var) + operator + str(divisor)))




def create_change_with_least_coins(change: int, coins: List[int]) -> List[int]:

    # brute force solution
    for i in range(1, len(coins) - 1):
        coin_permutation_subset = coins[:i]
        for coin_list in itertools.permutations(coin_permutation_subset):
            if sum(coin_list) == change:
                return list(coin_list)

    return None



CoinTotal = Dict[List[int], int]

def sum(list: List[int]) -> int:
    return functools.reduce(lambda x, y: x + y, list)


def main():
    path = "easytests/changecalc349_simple_input.txt"
    change_coins_lambda = parse_input(path)
    change_coins = change_coins_lambda[0]
    change = change_coins[0]
    coins = change_coins[1]
    func = change_coins_lambda[1]

    min_coins = create_change_with_least_coins(change, coins)

    if min_coins == None:
        # No solution was found
        print("No change!")
    elif func(len(min_coins)):
        for x in range(len(min_coins)):
            print(min_coins[x], end=' ')
    else:
        print("Too many coins!")


if __name__ == '__main__':
    main()

