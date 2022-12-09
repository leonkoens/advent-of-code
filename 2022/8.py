import re


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
grid_map = {}

size = len(grid)-1

for i in range(size+1):
    grid_map[(i, 0)] = 1
    grid_map[(0, i)] = 1
    grid_map[(i, size)] = 1
    grid_map[(size, i)] = 1


for i in range(size+1):
    a = grid[i][0]
    b = grid[0][i]
    c = grid[size-i][size]
    d = grid[size][size-i]

    for j in range(size+1):

        if grid[i][j] > a:
            grid_map[(i, j)] = 1
            a = grid[i][j]

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



#class Color:
#   PURPLE = '\033[95m'
#   CYAN = '\033[96m'
#   DARKCYAN = '\033[36m'
#   BLUE = '\033[94m'
#   GREEN = '\033[92m'
#   YELLOW = '\033[93m'
#   RED = '\033[91m'
#   BOLD = '\033[1m'
#   UNDERLINE = '\033[4m'
#   END = '\033[0m'
#
#
#for i in range(size+1):
#    for j in range(size+1):
#        if grid_map[(i,j)]:
#            print(Color.BLUE + str(grid[i][j]), end="")
#        else:
#            print(Color.RED + str(grid[i][j]), end="")
#    print()

print("Part 1, ", len([value for value in grid_map.values() if value]))


scenic_score_max = 0

for i in range(size+1):
    for j in range(size+1):
