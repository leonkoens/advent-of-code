from functools import reduce
from operator import mul


content = None
with open('8.txt', 'r') as handle:
    content = handle.readlines()

#content = """
#30373
#25512
#65332
#33549
#35390
#""".strip().split("\n")

grid = [[int(x) for x in list(line.strip())] for line in content]
size = len(grid)-1

grid_map = {}

for i in range(size+1):
    grid_map[(i, 0)] = 1
    grid_map[(0, i)] = 1
    grid_map[(i, size)] = 1
    grid_map[(size, i)] = 1


def scenic_score(i, j):
    height = grid[i][j]

    scenic = []

    lookaround = [True, True, True, True]
    score = 1

    if i == 0 or j == 0 or i == size or j == size:
        return 0

    while any(lookaround):
        if lookaround[0] and (i+score >= size or grid[i+score][j] >= height):
            lookaround[0] = False
            scenic.append(score)

        if lookaround[1] and (i-score <= 0 or grid[i-score][j] >= height):
            lookaround[1] = False
            scenic.append(score)

        if lookaround[2] and (j+score >= size or grid[i][j+score] >= height):
            lookaround[2] = False
            scenic.append(score)

        if lookaround[3] and (j-score <= 0 or grid[i][j-score] >= height):
            lookaround[3] = False
            scenic.append(score)

        score += 1

    if scenic:
        return reduce(mul, scenic)

    return 0

scenic_max = 0

for i in range(size+1):
    a = grid[i][0]
    b = grid[0][i]
    c = grid[size-i][size]
    d = grid[size][size-i]

    for j in range(size+1):

        if grid[i][j] > a:
            grid_map[(i, j)] = 1
            a = grid[i][j]
            scenic_max = max(scenic_max, scenic_score(i, j))

        if grid[j][i] > b:
            grid_map[(j, i)] = 1
            b = grid[j][i]

        if grid[size-i][size-j] > c:
            grid_map[(size-i, size-j)] = 1
            c = grid[size-i][size-j]        

        if grid[size-j][size-i] > d:
            grid_map[(size-j, size-i)] = 1
            d = grid[size-j][size-i]

        if (i, j) not in grid_map:
            grid_map[(i, j)] = 0


class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


for i in range(size+1):
    for j in range(size+1):
        if grid_map[(i,j)]:
            print(Color.BLUE + str(grid[i][j]), end="")
        else:
            print(Color.RED + str(grid[i][j]), end="")
    print()

print(Color.END)
print("Part 1", len([value for value in grid_map.values() if value]))
print("Part 2", scenic_max)


