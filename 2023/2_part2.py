import re

from dataclasses import dataclass
from operator import mul
from functools import reduce

from utils import InputReader


@dataclass
class AdventOfCode:

    total: int = 0

    def parse_line(self, line: str):
        regex_cubes = '((\d+) ([a-z]+))'

        cubes = re.findall(regex_cubes, line)

        cubes_needed = {
            'red': 0, 
            'green': 0,
            'blue': 0,
        }

        for cube in cubes:
            amount = int(cube[1])
            color = cube[2]
            cubes_needed[color] = max(cubes_needed[color], amount)

        self.total += reduce(mul, cubes_needed.values(), 1)


a = AdventOfCode()
InputReader('2.txt', a).read()

print(a.total)
