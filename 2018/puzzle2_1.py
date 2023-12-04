
content = ''
with open('input2.txt') as handle:
    content = handle.read().strip()


twos = 0
threes = 0
for box_id in content.split("\n"):
    
    counts = [box_id.count(c) for c in box_id]

    if 2 in counts:
        twos += 1

    if 3 in counts:
        threes += 1

print(twos * threes)
