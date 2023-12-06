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


just_once = []

regex = re.compile("^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
for claim in content.split("\n"):
    #1 @ 338,764: 20x24

    match = regex.match(claim)
    claim_id = int(match.group(1))
    from_left = int(match.group(2))
    from_top = int(match.group(3))
    width = int(match.group(4))
    height = int(match.group(5))
    
    only_this_one = True
    to_remove = set()
    i = from_left
    while i < (from_left+width):
        j = from_top
        while j < (from_top+height):
            fabric[i][j].append(claim_id)
            position_length = len(fabric[i][j])
            
            if position_length > 1:
                only_this_one = False
                for other_claim_id in fabric[i][j]:
                    to_remove.add(other_claim_id)

            j += 1
        i += 1
    
    if only_this_one:
        just_once.append(claim_id)
    else:
        for other_claim_id in to_remove:
            try:
                just_once.remove(other_claim_id)
            except ValueError:
                pass

print(just_once[0])
