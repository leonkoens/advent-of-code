import sys
from collections import deque


with open('input_10.txt') as f:
#with open('input_10_test2.txt') as f:
    content = f.read().strip().split("\n")


adapters = [int(x) for x in content]
adapters.sort()
adapters.append(max(adapters) + 3)

nodes = []
leaves_finished = []
finished = 0

class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def __repr__(self):
        return str(self.value)


root = Node(0, 0)
leaves = deque([root])
number_of_adapters = len(adapters)

try:
    while True:
        node = leaves.pop()

        if node.index == number_of_adapters-1:
            finished += 1
            continue
            

        i = node.index
        while True:

            if (adapters[i] - node.value) > 3:
                break

            a = Node(adapters[i], i+1)
            leaves.append(a)

            i += 1

except IndexError:
    print(finished)
