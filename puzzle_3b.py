
content = None

with open('input_3.txt', 'r') as handle:
    content = handle.readlines()


first = content[0]
second = content[1]

locations = set()
location = [0, 0]

steps_dict = dict()
steps = 0

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

    else:
        import pbd;pdb.set_trace()

    for _ in range(length):
        location[0] += new_location[0]
        location[1] += new_location[1]

        steps += 1

        try:
            if steps < steps_dict[tuple(location)]:
                steps_dict[tuple(location)] = steps
        except KeyError:
            steps_dict[tuple(location)] = steps

        locations.add(tuple(location))


location = [0, 0]
steps = 0

lowest = 999999999999

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

    else:
        import pbd;pdb.set_trace()

    for _ in range(length):
        location[0] += new_location[0]
        location[1] += new_location[1]

        steps += 1

        if tuple(location) in locations:

            lowest = min(lowest, steps + steps_dict[tuple(location)])

print(lowest)
