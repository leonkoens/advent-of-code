import sys
import re


with open('input_6.txt') as f:
    content = f.read().strip().split("\n")


groups = []
group = [set(), 0]

total = 0

for line in content:

    if line == '':
        total += len(group[0])
        groups.append(group)
        group = [set(), 0]
        continue

    for char in line:
        group[0].add(char)
    
    group[1] += 1

total += len(group[0])
print(total)

