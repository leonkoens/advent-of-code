import re


content = None
with open('4.txt', 'r') as handle:
    content = handle.readlines()

#content = """MMMSXXMASM
#MSAMXMSMSA
#AMXSXMAAMM
#MSAMASMSMX
#XMASAMXAMM
#XXAMMXXAMA
#SMSMSASXSS
#SAXAMASAAA
#MAMMMXMMMM
#MXMXAXMASX""".splitlines()

field = [list(line) for line in content]

found = 0

for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] != 'A':
            continue

        if i-1 < 0 or i+1 >= len(field):
            continue
        
        if j-1 < 0 or j+1 >= len(field[i]):
            continue

        pair_a = set([field[i-1][j-1], field[i+1][j+1]])
        pair_b = set([field[i-1][j+1], field[i+1][j-1]])

        if 'X' in pair_a or 'X' in pair_b or 'A' in pair_a or 'A' in pair_b:
            continue

        if len(pair_a) != 2 or len(pair_b) != 2:
            continue
        
        found += 1

print(found)