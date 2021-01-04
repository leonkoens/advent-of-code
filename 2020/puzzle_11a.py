import copy
import sys


#with open('input_11_test.txt') as f:
with open('input_11.txt') as f:
    content = f.read().strip().split("\n")

area = [list(x) for x in content]
changes = True
new_area = None

def check_seats(x, y):
    
    occupied = 0

    for ya in [-1, 0, 1]:
        for xa in [-1, 0, 1]:
            if xa == 0 and ya == 0:
                continue
            
            if x == 0 and xa == -1:
                continue

            if y == 0 and ya == -1:
                continue

            try:
                if area[y + ya][x + xa] == '#':
                    occupied += 1
            except IndexError:
                pass

    return occupied




rounds = 0
while changes:
    changes = False
    new_area = copy.deepcopy(area)

    for i in range(len(area)):
        for j in range(len(area[0])):
            
            if area[i][j] == '.':
                continue

            occupied = check_seats(j, i)

            if area[i][j] == 'L' and occupied == 0:
                new_area[i][j] = '#'
                changes = True

            elif area[i][j] == '#' and occupied >= 4:
                new_area[i][j] = 'L'
                changes = True

    rounds += 1
    area = copy.deepcopy(new_area)

total = 0
for line in area:
    total += line.count('#')

print(total)
