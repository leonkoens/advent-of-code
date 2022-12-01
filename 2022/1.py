
content = None
with open(__file__.replace('.py', '.txt'), 'r') as handle:
    content = handle.readlines()

calories_max = 0
subtotal = 0
calories = []

for line in content:

    if line.strip() == '':
        calories.append(subtotal)
        subtotal = 0
        continue
    
    subtotal += int(line)
    calories_max = max(subtotal, calories_max)

print("Part 1", calories_max)
print("Part 2", sum(sorted(calories)[-3:]))

