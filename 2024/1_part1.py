import math

content = None
with open('1.txt', 'r') as handle:
    content = handle.readlines()

list_a = []
list_b = []

for line in content:
    a, b = line.split()

    list_a.append(int(a))
    list_b.append(int(b))

list_a.sort()
list_b.sort()

distance = 0
for i in range(len(list_a)):

    distance += abs(list_a[i] - list_b[i])

print(distance)
    
