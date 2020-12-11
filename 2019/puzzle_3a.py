
content = None

with open('input_3.txt', 'r') as handle:
    content = handle.readlines()


first = content[0]
second = content[1]

distance = 9999999

locations = set()
location = [0, 0]

for update in first.split(','):

    direction = update[0]
    new_location = (0, 0)

    length = int(update[1:])

    if direction == 'R':
        new_location = (+1, 0)

    elif direction == 'L':
        new_location = (-1, 0)

    elif direction == 'U':
        new_location = (0, +1)

    elif direction == 'D':
        new_location = (0, -1)

    for _ in range(length):
        location[0] += new_location[0]
        location[1] += new_location[1]

        locations.add(tuple(location))


location = [0, 0]

for update in second.split(','):

    direction = update[0]
    new_location = (0, 0)

    length = int(update[1:])

    if direction == 'R':
        new_location = (+1, 0)

    elif direction == 'L':
        new_location = (-1, 0)

    elif direction == 'U':
        new_location = (0, +1)

    elif direction == 'D':
        new_location = (0, -1)

    for _ in range(length):
        location[0] += new_location[0]
        location[1] += new_location[1]

        if tuple(location) in locations:
            distance = min(distance, abs(location[0]) + abs(location[1]))

print(distance)
