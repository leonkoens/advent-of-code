import sys


with open('input_9.txt') as f:
    content = [int(x) for x in f.read().strip().split("\n")]

target = 756008079

contiguous = []

for number in content:

    contiguous.append(number)

    while sum(contiguous) > target:
        contiguous.pop(0)
    
    if sum(contiguous) == target:
        print(min(contiguous) + max(contiguous))
        sys.exit()
