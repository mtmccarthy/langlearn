from typing import List, Tuple

"""
A solution to the intermediate challenge #350 Balancing My Spending
https://www.reddit.com/r/dailyprogrammer/comments/7vx85p/20180207_challenge_350_intermediate_balancing_my/

"""

EquilIndex = Tuple[int, int, int, int]  # (index, before_sum, after_sum)


def parse_input(path: str) -> List[int]:
    input_file = open(path, 'r')
    lines = input_file.readlines()
    input_file.close()

    numbers_on_second_line = int(lines[0])
    second_line = lines[1]

    num_strs = second_line.split(" ", numbers_on_second_line)

    return list(map(lambda num: int(num), num_strs))


def generate_index_value(nums: List[int]) -> List[EquilIndex]:

    equil_indexes = []

    for i, value in enumerate(nums):
        equil_index = (i, value, 0, 0) # Deliberately 0 and will be calculated later
        equil_indexes.append(equil_index)

    return equil_indexes


def generate_before_sum(list: List[EquilIndex]) -> List[EquilIndex]:
    before_sum_count = 0
    new_list = []
    for entry in list:
        index = entry[0]
        value = entry[1]
        if index == 0:
            new_entry = (index, value, 0, 0) #After sum calculated later
        else:
            prev_entry = new_list[index - 1]
            prev_value = prev_entry[1]
            prev_sum = prev_entry[2]
            new_entry = (index, value, prev_sum + prev_value, 0)

        new_list.append(new_entry)

    return new_list


def generate_after_sum(list: List[EquilIndex]) -> List[EquilIndex]:
    new_list = []
    for entry in reversed(list):
        index = entry[0]
        value = entry[1]
        before_sum = entry[2]

        if index == len(list) - 1:
            new_entry = (index, value, before_sum, 0)
        else:
            later_entry = new_list[len(list) - index - 2]
            later_value = later_entry[1]
            later_after_sum = later_entry[3]
            new_entry = (index, value, before_sum, later_after_sum + later_value)

        new_list.append(new_entry)

    return new_list[::-1]  # Reverse the list in correct order

def calc_equilibrium_indexes(nums: List[int]) -> List[int]:
    equil_indexes = generate_index_value(nums)
    before_sum_indexes = generate_before_sum(equil_indexes)
    return generate_after_sum(before_sum_indexes)


def main():
    path = "./intermediate_tests/350_simple_input.txt"
    nums = parse_input(path)
    indexes = calc_equilibrium_indexes(nums)

    for index in indexes:
        if index[2] == index[3]:
            print(index[0])


if __name__ == "__main__":
    main()