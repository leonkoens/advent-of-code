
content = None
with open(__file__.replace('.py', '.txt'), 'r') as handle:
    content = handle.readlines()

convert = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
win_table = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

lose_table = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3,
}

total = 0

for line in content:
    other, me = line.split()

    total += scores[me]

    if other == convert[me]:
        total += 3

    elif win_table[other] != me:
        total += 6


print("Part 1", total)



# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

total = 0

for line in content:
    other, me = line.split()

    if me == 'Y':
        total += 3
        total += scores[other]

    elif me == 'X':
        total += scores[win_table[other]]

    elif me == 'Z':
        total += scores[lose_table[other]]
        total += 6


print("Part 2", total)
