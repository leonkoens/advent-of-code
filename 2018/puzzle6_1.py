import string

content = ''
with open('input6.txt') as handle:
    content = handle.read().strip()

points = [line.split(",") for line in content.split("\n")]
area_size = {}
infinite = set()
max_size = 358

for i in range(max_size):

    for j in range(max_size):

        shortest = 999999999999999999999999999999999999999999
        shortest_index = -1

        for k in range(len(points)):
            distance = abs(i - int(points[k][0])) + abs(j - int(points[k][1]))

            if distance < shortest:
                shortest = distance
                shortest_index = k

            elif distance == shortest:
                shortest_index = -1

        if i == 0 or j == 0 or i == max_size-1 or j == max_size-1:
            infinite.add(shortest_index)

        try:
            area_size[shortest_index] += 1
        except KeyError:
            area_size[shortest_index] = 1

for index in infinite:
    area_size.pop(index)

print(max(area_size.values()))
