from dataclasses import dataclass
from functools import reduce
import re


content = None
with open('3.txt', 'r') as handle:
    content = handle.readlines()


class Number:

    def __init__(self):
        self.number = None
        self.parts = []
    
    def __repr__(self) -> str:
        return ''.join(self.parts)
    
    def get_number(self):
        return int(''.join(self.parts))



class AdventOfCode:

    def __init__(self, content):
        self.grid = [list(line.strip()) for line in content]
        self.symbol_regex = re.compile('[^a-z0-9\.]')
        self.number_regex = re.compile('[0-9]')
        self.numbers_map = {}

    def run(self):
        symbol_locations = []

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                value = self.grid[i][j]

                match = self.number_regex.search(value)
                if match:
                    if current_number is None:
                        current_number = Number()

                    current_number.parts.append(value)
                    self.numbers_map[(i, j)] = current_number

                else:
                    current_number = None


                match = self.symbol_regex.search(value)
                if match:
                    symbol_locations.append((i, j))
        
        total = 0
        numbers_set = set()
        for y, x in symbol_locations:
            locations = [
                (y-1, x-1),
                (y-1, x),
                (y-1, x+1),
                (y, x-1),
                (y, x+1),
                (y+1, x-1),
                (y+1, x),
                (y+1, x+1),
            ]

            for location in locations:
                if location in self.numbers_map:
                    numbers_set.add(self.numbers_map[location])

        print(sum([number.get_number() for number in numbers_set]))


aoc = AdventOfCode(content)
aoc.run()