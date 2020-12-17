import sys


with open('input_10.txt') as f:
    content = f.read().strip().split("\n")

adapters = [int(x) for x in content]
adapters.sort()
adapters.insert(0, 0)
adapters.append(max(adapters)+3)

combinations = dict()
combinations[0] = 1


for i  in range(0, len(adapters)):
    for j in range(i+1, len(adapters)):
        
        diff = adapters[j] - adapters[i]

        if diff > 3:
            break

        try:
            combinations[adapters[j]] += combinations[adapters[i]]
        except KeyError:
            combinations[adapters[j]] = combinations[adapters[i]]

print(combinations[max(adapters)])
