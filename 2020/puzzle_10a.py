import sys


with open('input_10.txt') as f:
    content = f.read().strip().split("\n")


adapters = [int(x) for x in content]
adapters.sort()

adapters.insert(0, 0)

ones = 0
threes = 0

for i in range(len(adapters)):

    try:
        diff = adapters[i+1] - adapters[i]

        if diff == 1:
            ones += 1

        if diff == 3:
            threes += 1

    except IndexError:
        threes += 1

print(ones * threes)
