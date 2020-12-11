import sys


with open('input_3.txt') as f:
    content = f.read()

content = [x for x in content.strip().split("\n")]

x = 0
width = len(content[0])
y = 0 

trees = 0

while y < len(content):

    if content[y][x] == '#':
        trees += 1

    x = (x + 3) % width
    y += 1

print(trees)
