import re
from typing import DefaultDict


content = None
with open('5.txt', 'r') as handle:
    content = handle.readlines()

#content = """47|53
#97|13
#97|61
#97|47
#75|29
#61|13
#75|53
#29|13
#97|29
#53|29
#61|53
#97|53
#61|29
#47|13
#75|47
#97|75
#47|61
#75|61
#47|29
#75|13
#53|13
#
#75,47,61,53,29
#97,61,53,29,13
#75,29,13
#75,97,47,61,53
#61,13,29
#97,13,75,29,47""".splitlines()

rules = DefaultDict(set)
rules_done = False
middles = 0

for line in content:

    line = line.strip()

    if line == '':
        rules_done = True
        continue

    if not rules_done:
        a, b = line.split('|')
        rules[a].add(b)

    else:
        numbers = line.split(',')
        size = len(numbers)-1
        good = True

        for i in range(size):
            to_check = numbers[size-i]
            check_against = numbers[0:size-i]

            if rules[to_check].intersection(set(check_against)):
                good = False
                break
                
        if good:
            middles += int(numbers[size//2])

print(middles)

