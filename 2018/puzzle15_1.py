
content = ''
with open('input15_test.txt') as handle:
    content = handle.read().strip()
 
elves = []
goblins = []
players = []

grid = [list(line) for line in content.split("\n")]

print(grid)

for i, line in enumerate(grid):
    for j, loc in enumerate(line):
        if loc == 'E':
            elves.append((i, j))
            players.append([i, j, 'E'])

        elif loc == 'G':
            goblins.append((i, j))
            players.append([i, j, 'G'])


print(elves)
print(goblins)


while True:

    #players = sorted(players, key=lambda x: (x[0], x[1]))
    players = sorted(players)

    for player in players:
        pass

    
    
