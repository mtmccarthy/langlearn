from common import *
from typing import Union

"""
Finds the greatest exponent of n that is less than or equal to another number m
Example: if n = 2 and m = 17 return 4
"""


def get_base62_character(index: int) -> Union[str, None]:
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    if index < 10:
        return str(index)
    elif 10 <= index < 36:
        return lower_case[index - 10]
    elif 36 <= index < 62:
        return capital_letters[index - 36]
    else:
        return None


def find_greatest_exponent_of_n_loe_than_m(n: int, m: int) -> int:
    current_exponent = 0
    while n ** current_exponent <= m:
        current_exponent += 1
    return current_exponent - 1


def convert_from_base10ton(baseN: int, num: int) -> str:
    conversion = []
    power = find_greatest_exponent_of_n_loe_than_m(baseN, num)
    while power > 0:
        place_value = baseN ** power
        digit = 0
        while num - place_value > 0:
            digit += 1
            num -= place_value
        conversion.append(digit)
        power -= 1

    conversion.append(num)  # One's place

    return ''.join(list(map(lambda digit: get_base62_character(digit), conversion)))


def generate_output(path: str) -> str:
    lines = get_file_lines(path)
    output = ""

    for line in lines:
        output += convert_from_base10ton(62, int(line.rstrip())) + '\n'

    return output


def main():
    path = 'easytests/imgurlinks_352_challenge_input.txt'
    print(generate_output(path))


if __name__ == '__main__':
    main()
