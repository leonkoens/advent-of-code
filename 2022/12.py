import sys


content = None
with open(__file__.replace('.py', '.txt'), 'r') as handle:
    content = handle.readlines()


#content = """
#Sabqponm
#abcryxxl
#accszExk
#acctuvwj
#abdefghi
#""".strip().split("\n")


class Node:

    def __init__(self, value, coords):

        self.value = value
        self.steps = sys.maxsize

        if value == 'S':
            self.value = 'a'
            self.steps = 0

        if value == 'E':
            self.value = 'z'

        self.int_value = ord(self.value)
        self.coords = coords
        self.vertices = []
        self.parent = None

    def __repr__(self):
        return f'{self.coords} {self.value} {self.steps}'


grid = [list(line.strip()) for line in content]
grid_map = {}
end = None
start = None
a = []

for i in range(len(grid)):
    for j in range(len(grid[0])):

        if (i,j) not in grid_map:
            node = Node(grid[i][j], (i,j))
            grid_map[(i, j)] = node
        else:
            node = grid_map[(i, j)]

        if grid[i][j] == 'S':
            start = node

        if grid[i][j] == 'E':
            end = node

        if grid[i][j] == 'a':
            a.append(node)

        for check in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n_square = (i + check[0], j + check[1])

            try:
                n_height = grid[n_square[0]][n_square[1]]
            except IndexError:
                continue
            
            if n_square not in grid_map:
                n_node = Node(grid[n_square[0]][n_square[1]], n_square)
                grid_map[n_square] = n_node
            else:
                n_node = grid_map[n_square]

            if n_node.int_value - node.int_value <= 1:
                node.vertices.append(n_node)


def find_route(start, end):

    pq = [start]
    route = []

    while True:

        try:
            node = pq.pop()
        except IndexError:
            break
        
        for vertice in node.vertices:
            new_steps = node.steps + 1

            if vertice.steps > new_steps:
                vertice.steps = new_steps
                vertice.parent = node

                pq.append(vertice)

                if vertice.coords == end.coords:
                    return vertice.steps


        pq.sort(key=lambda x: x.steps, reverse=True)
    
    return sys.maxsize


print("Part 1", find_route(start, end))

shortest = sys.maxsize

for start in a:

    for value in grid_map.values():
        value.steps = sys.maxsize

    start.steps = 0
    shortest = min(find_route(start, end), shortest)

print("Part 2", shortest)

