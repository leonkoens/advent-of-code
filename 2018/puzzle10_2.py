import re

content = ''
with open('input10.txt') as handle:
    content = handle.read().strip()

regex = re.compile("position=<( ?-?[0-9]+), ( ?-?[0-9]+)> velocity=<( ?-?[0-9]+), ( ?-?[0-9]+)>")

points = []

for line in content.split("\n"):
    
    match = regex.match(line)

    pos_x = int(match.group(1))
    pos_y = int(match.group(2))
    vel_x = int(match.group(3))
    vel_y = int(match.group(4))

    point = [pos_x, pos_y, vel_x, vel_y]
    points.append(point)


def transform_points(points, negative):
    if negative is True:
        for point in points:
            point[0] -= point[2]
            point[1] -= point[3]
    else:
        for point in points:
            point[0] += point[2]
            point[1] += point[3]

    return points

lowest_x = 9999999999
lowest_y = 9999999999
for i in range(16000):
    
    points = transform_points(points, False)

    x_max = max([p[0] for p in points])
    x_min = min([p[0] for p in points])


    x_diff = x_max - x_min

    y_max = max([p[1] for p in points])
    y_min = min([p[1] for p in points])

    
    if x_min < 0 or y_min < 0:
        continue

    y_diff = y_max - y_min

    if y_diff < lowest_x and x_diff < lowest_x:
        lowest_x = x_diff
        lowest_y = y_diff

    else:
        break

points = transform_points(points, True)

for point in points:
    point[0] -= 155
    point[1] -= 190

x_min = min([p[0] for p in points])
x_max = max([p[0] for p in points])
y_min = min([p[1] for p in points])
y_max = max([p[1] for p in points])

both_max = max(x_max, y_max)
both_min = max(x_min, y_min)

grid = []
for k in range(y_max+3):
    grid.append([])
    for j in range(x_max+3):
        grid[k].append('.')

for point in points:
    try:
        grid[point[1]][point[0]] = 'x'
    except IndexError:
        pass

print(i)
