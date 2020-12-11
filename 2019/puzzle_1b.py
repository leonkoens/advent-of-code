import math


content = None

with open('input_1.txt', 'r') as handle:
    content = handle.readlines()

fuel = 0

for number in content:
    required_fuel = (math.floor(int(number) / 3) - 2)

    while required_fuel > 0:
        fuel += required_fuel
        required_fuel = (math.floor(required_fuel / 3) - 2)

print(fuel)
