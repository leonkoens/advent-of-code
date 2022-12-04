
content = None
with open(__file__.replace('.py', '.txt'), 'r') as handle:
    content = handle.readlines()

#content = """
#vJrwpWtwJgWrhcsFMMfFFhFp
#jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
#PmmdzqPrVvPwwTWBwg
#wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
#ttgJtRGJQctTZtZT
#CrZsJsPPZsGzwwsLwLmpwMDw
#""".strip().split("\n")

total_part1 = 0
total_part2 = 0
group = []

def calculate_score(character):
    score = ord(character)

    if score <= 90:
        score -= 38
    else:
        score -= 96
    
    return score

for line in content:
    line = line.strip()
    compartment_1 = set(list(line[int(len(line)/2):]))
    compartment_2 = set(list(line[:int(len(line)/2)]))

    group.append(line)

    if len(group) == 3:
        sacks = [set(list(a)) for a in group]
        badge = sacks[0].intersection(sacks[1]).intersection(sacks[2])
        total_part2 += calculate_score(list(badge)[0])
        group = []


    intersection = compartment_1.intersection(compartment_2)

    total_part1 += calculate_score(list(intersection)[0])


print("Part 1", total_part1)
print("Part 2", total_part2)
