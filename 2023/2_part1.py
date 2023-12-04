import re

from dataclasses import dataclass

from utils import InputReader


@dataclass
class AdventOfCode:

    total: int = 0
    cubes_available: dict = None

    def __post_init__(self):
        self.cubes_available = {
            'red': 12, 
            'green': 13,
            'blue': 14,
        }

    def parse_line(self, line: str):
        regex_game = 'Game (\d+)'
        regex_cubes = '((\d+) ([a-z]+))'

        game = re.findall(regex_game, line)
        cubes = re.findall(regex_cubes, line)

        possible = []

        for cube in cubes:
            amount = int(cube[1])
            color = cube[2]

            possible.append(self.cubes_available[color] >= amount)

        if all(possible):
            self.total += int(game[0])


a = AdventOfCode()
InputReader('2.txt', a).read()

print(a.total)
