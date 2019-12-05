
content = None

with open('input_3.txt', 'r') as handle:
    content = handle.readlines()


first = content[0]
second = content[1]


locations = set()
location = [0, 0]

for update in first.split(','):

    direction = update[0]
    new_location = (0, 0)

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

    location[0] += new_location[0]
    location[1] += new_location[1]

    locations.add(location)

print(locations)
