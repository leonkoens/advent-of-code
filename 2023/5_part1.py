from dataclasses import dataclass
import re


content = None
#with open('5_test.txt', 'r') as handle:
with open('5.txt', 'r') as handle:
    content = handle.readlines()


class Category:

    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.maps_to = None

        self.connections = {}
    
    def __repr__(self):
        return f'{self.name}: {self.start} - {self.end}'
    

class AdventOfCode:

    def __init__(self, content):
        self.content = content

    def run(self):

        seeds = []
        category_map = {
            'seed': {},
            'soil': {},
            'fertilizer': {},
            'water': {},
            'light': {},
            'temperature': {},
            'humidity': {},
            'location': {},
        }
        source = None

        for line in self.content:
            if line.strip() == '':
                continue

            match = re.search('^seeds: (.+)', line)

            if match:
                seeds = match.group(1).split(' ')
                continue
            
            match = re.search('([a-z]+)-to-([a-z]+) map:', line)

            if match:
                source = match.group(1)
                continue
            
            drs, srs, r = map(int, line.split(' '))
            category_map[source][range(srs, srs+r)] = srs, drs
                
        lowest = 9999999999999999999

        for seed in seeds:
            current = int(seed)

            for category in category_map.keys():

                for cr in category_map[category].keys():

                    if current in cr:
                        starts = category_map[category][cr]
                        current -= starts[0]
                        current += starts[1]
                        break

            lowest = min(lowest, current)

        print(lowest)

aoc = AdventOfCode(content)
aoc.run()