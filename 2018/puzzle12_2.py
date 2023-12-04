import re


# Awnsers: 2550000000934 -> too high

content = ''
with open('input12.txt') as handle:
    content = handle.read().strip()

generations = 50000000000
#generations = 75000

match = re.match("initial state: (.+)", content)
plants = match.group(1)
first = 0
plant_count = 0
running_plant_count = []

groth = {}

for match in re.findall("([.#]{5}) => (\.|#)", content):
    groth[match[0]] = match[1]


for i in range(generations):

    if plants[-5:] != '.....':
        plants = plants + '.....'

    if plants[:5] != '.....':
        plants = '.....' + plants
        first += 5

    new_plants = "." * len(plants)
    new_plants = list(new_plants)

    for search, replace in groth.items():
        start = 0

        if search not in plants:
            continue 

        while True:
            index = plants.find(search, start+1)
            
            if index == -1:
                break

            start = index

            #import pdb;pdb.set_trace()
            new_plants[start+2] = replace

    plants = "".join(new_plants)

    running_plant_count.append(plants.count('#'))

    if running_plant_count[-3:] == [running_plant_count[-1]] * 3:
        break


total = 0
for j in range(len(plants)):
    index = j - first + ((generations-1) - i)

    if plants[j] == '#':
        total += index 

print(total)

