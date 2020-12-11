import sys


with open('input_3.txt') as f:
    content = f.read()

content = [x for x in content.strip().split("\n")]

width = len(content[0])

increments = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

trees_product = 0

for increment in increments:
    trees = 0
    x = 0
    y = 0 

    while y < len(content):

        if content[y][x] == '#':
            trees += 1

        x = (x + increment[0]) % width
        y += increment[1]

    if trees_product == 0:
        trees_product = trees
    else:
        trees_product *= trees


print(trees_product)
