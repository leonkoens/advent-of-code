
import string
from typing import List

with open('input5.txt', 'r') as file:
    lines = [line for line in file.readlines()]

polymer = lines[0]


def react(chain: List[str]):
    i = 0
    run = True

    while run:
        first = chain[i]
        second = chain[i + 1]

        if first.lower() == second.lower() and first != second:
            chain = chain[0:i] + chain[i + 2:]
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1

        if i == len(chain) - 1:
            run = False

    return chain


print('Reacted polymer length: {}'.format(len(react(list(polymer)))))

