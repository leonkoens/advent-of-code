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


def check(field, i, j, k, l):
    xmas = list("MAS")

    if k == 0 and l == 0:
        return False

    x = j
    y = i

    for m in range(3):
        x += l
        y += k

        if y < 0 or y >= len(field):
            return False

        if x < 0 or x >= len(field[i]):
            return False
                        
        if field[y][x] != xmas[m]:
            return False
    
    return True


found = 0

for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] != 'X':
            continue

        for k in (-1, 0, 1):
            for l in (-1, 0, 1):

                if check(field, i, j, k, l):
                    found += 1

print(found)