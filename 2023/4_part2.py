from dataclasses import dataclass
from functools import reduce
import re


content = None
with open('4.txt', 'r') as handle:
    content = handle.readlines()


class AdventOfCode:

    def __init__(self, content):
        self.content = content
        self.game_copies = dict(zip(range(1, len(self.content)+1), [1] * len(self.content)))
    
    def score_card(self, card):
        winning, actual = card.split(':')[1].split(' | ')

        winning_numbers = set(re.findall('(\d+)', winning))
        actual_numbers = set(re.findall('(\d+)', actual))

        win = winning_numbers.intersection(actual_numbers)

        return len(win)

    def run(self):
        for line in self.content:
            game = int(re.findall('(\d+): ', line)[0])
            points = self.score_card(line)

            if points == 0:
                continue

            for i in range(game+1, game+points+1):
                self.game_copies[i] += self.game_copies[game]
        
        print(sum(self.game_copies.values()))


aoc = AdventOfCode(content)
aoc.run()