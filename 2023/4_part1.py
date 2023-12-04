from dataclasses import dataclass
from functools import reduce
import re


content = None
with open('4.txt', 'r') as handle:
    content = handle.readlines()


class AdventOfCode:

    def __init__(self, content):
        self.content = content

    def run(self):

        total = 0
        for line in self.content:
            winning, actual = line.split(':')[1].split(' | ')

            winning_numbers = set(re.findall('(\d+)', winning))
            actual_numbers = set(re.findall('(\d+)', actual))

            win = winning_numbers.intersection(actual_numbers)

            if win:
                total += 1 << len(win) - 1

        print(total)

aoc = AdventOfCode(content)
aoc.run()