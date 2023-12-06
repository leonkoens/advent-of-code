
content = ''
with open('input6.txt') as handle:
    content = handle.read().strip()

points = [line.split(",") for line in content.split("\n")]
area_size = 0
max_size = 358

for i in range(max_size):
    for j in range(max_size):
        distance = sum([abs(i - int(points[k][0])) + abs(j - int(points[k][1])) for k in range(len(points))])
        if distance < 10000:
            area_size += 1
            
print(area_size)
