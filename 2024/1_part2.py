from typing import Counter

content = None
with open('1.txt', 'r') as handle:
    content = handle.readlines()

list_a = []
list_b = []

for line in content:
    a, b = line.split()

    list_a.append(int(a))
    list_b.append(int(b))

counter_b = Counter(list_b)

similarity = 0
for item in list_a:

    similarity += item * counter_b[item]

print(similarity)
    
