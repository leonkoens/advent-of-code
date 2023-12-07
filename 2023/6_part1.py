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

        data = dict(zip(
            map(int, re.findall('(\d+)', self.content[0])),
            map(int, re.findall('(\d+)', self.content[1]))
        ))

        totals = []

        for ms, record in data.items():
            sub_total = 0

            for i in range(ms):
                distance = i* (ms - i)

                if distance > record:
                    sub_total += 1
            
            totals.append(sub_total)
        
        print(reduce(mul, totals))
        


aoc = AdventOfCode(content)
aoc.run()