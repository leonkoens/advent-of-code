import math


content = None

with open('input1.txt', 'r') as handle:
    content = handle.readlines()

fuel = 0

for number in content:
    fuel += (math.floor(int(number) / 3) - 2)

print(fuel)
