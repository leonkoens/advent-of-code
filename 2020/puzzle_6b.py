import sys
import re


with open('input_6.txt') as f:
    content = f.read().strip().split("\n")


groups = []
group = [{}, 0]

total = 0

for line in content:

    if line == '':
        for q in group[0]:
            if group[0][q] == group[1]:
                total += 1
        
        groups.append(group)
        group = [{}, 0]
        continue

    for char in line:
        try:
            group[0][char] += 1
        except KeyError:
            group[0][char] = 1
            
    
    group[1] += 1

for q in group[0]:
    if group[0][q] == group[1]:
        total += 1

print(total)
