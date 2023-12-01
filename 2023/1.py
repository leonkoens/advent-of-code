import re

content = None
#with open(__file__.replace('.py', '.txt'), 'r') as handle:
with open('1_sjoerd.txt', 'r') as handle:
    content = handle.readlines()

number_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

total_part_1 = 0
total_part_2 = 0

def extract_number_part_1(line):
    regex = '^.*?([0-9])'

    match = re.search(regex, line)
    first = match.group(1)

    match = re.search(regex, line[::-1])
    second = match.group(1)

    return int(first + second)


def extract_number_part_2(line):
    numbers = '|'.join(number_map.keys())

    regex = f"^.*?([0-9]|{numbers})"
    match = re.search(regex, line)
    first = match.group(1)

    if first in number_map:
        first = number_map[first]

    regex = f"^.*?([0-9]|{numbers[::-1]})"
    match = re.search(regex, line[::-1])
    second = match.group(1)[::-1]

    if second in number_map:
        second = number_map[second]

    return int(first + second)


for line in content:
    line = line.strip()

    if line == '':
        continue

    total_part_1 += extract_number_part_1(line)
    total_part_2 += extract_number_part_2(line)


print('part 1', total_part_1)
print('part 2', total_part_2)

