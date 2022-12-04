
content = None
with open(__file__.replace('.py', '.txt'), 'r') as handle:
    content = handle.readlines()

#content = """
#2-4,6-8
#2-3,4-5
#5-7,7-9
#2-8,3-7
#6-6,4-6
#2-6,4-8
#""".strip().split("\n")


total_part1 = 0
total_part2 = 0
for line in content:
    first, second = [[int(b) for b in a.split("-")] for a in line.split(",")]

    if first[0] <= second[0] and first[1] >= second[1]:
        total_part1 += 1
        
    elif second[0] <= first[0] and second[1] >= first[1]:
        total_part1 += 1

    if set(range(first[0], first[1]+1)).intersection(range(second[0], second[1]+1)):
        total_part2 += 1


print("Part1", total_part1)
print("Part2", total_part2)

