import sys

from random import *
"""
A solution to hard challenge #350 Which Number Recurs First

https://www.reddit.com/r/dailyprogrammer/comments/7wfd0n/20180209_challenge_350_hard_which_number_recurs/

Working with very large data sets is an increasingly common activity in efforts such as web analytics and Internet advertising. Efficiently keeping track of values when you have around 264 possible values is the challenge.

Today's challenge is to read a steady stream of distinct values and report on the first one that recurs. Your program should be able to run an arbitrary number of times with distinct, infinite sequences of input and yield the correct value.

"""


def generate_random_stream():
    while True:
        yield randint(0, sys.maxsize)


def main():
    random_stream = generate_random_stream()
    hash_table = dict()

    for random_int in random_stream:
        if random_int in hash_table.keys():
            print("First repeating integer: " + str(random_int))
            return random_int
        else:
            hash_table[random_int] = 1


if __name__ == "__main__":
    main()