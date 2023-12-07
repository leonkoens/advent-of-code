from dataclasses import dataclass
from functools import reduce
from operator import mul
import re


content = None
with open('6.txt', 'r') as handle:
    content = handle.readlines()


class AdventOfCode:

    def __init__(self, content):
        self.content = content

    def run(self):

        ms = 40817772
        record = 219101213651089
        total = 0

        for i in range(ms):
            distance = i * (ms - i)

            if distance > record:
                total += 1
            
        print(total)


aoc = AdventOfCode(content)
aoc.run()