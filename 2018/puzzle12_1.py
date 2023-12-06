import re

content = ''
with open('input12.txt') as handle:
    content = handle.read().strip()

generations = 20

match = re.match("initial state: (.+)", content)
plants = match.group(1)
first = 0

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
        while True:
            index = plants.find(search, start+1)
            
            if index == -1:
                break

            start = index

            #import pdb;pdb.set_trace()
            new_plants[start+2] = replace

    plants = "".join(new_plants)

total = 0
for i in range(len(plants)):
    index = i - first

    if plants[i] == '#':
        total += index 

print(total)
