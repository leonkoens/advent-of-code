import re
import sys

content = ''
with open('input3.txt') as handle:
    content = handle.read().strip()


fabric = []

i = j = 0
while i < 1000:
    fabric.append([])
    j = 0
    while j < 1000:
        fabric[i].append([])
        j += 1
    i +=1


two_or_more = 0

regex = re.compile("^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
for claim in content.split("\n"):
    #1 @ 338,764: 20x24

    match = regex.match(claim)
    claim_id = int(match.group(1))
    from_left = int(match.group(2))
    from_top = int(match.group(3))
    width = int(match.group(4))
    height = int(match.group(5))
    
    i = from_left
    while i < (from_left+width):
        j = from_top
        while j < (from_top+height):
            fabric[i][j].append(claim_id)
            if len(fabric[i][j]) == 2:
                two_or_more += 1

            j += 1
        i += 1

print(two_or_more)
