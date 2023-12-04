import string
import re


class Node:

    def __init__(self, child_length, meta_length):
        self.child_length = child_length
        self.meta_length = meta_length

        self.parent = None
        self.meta = None
        self.children = []


content = ''
with open('input8.txt') as handle:
    content = handle.read().strip().split(" ")

nodes = []
parent = None
current = None

i = 0
while i < len(content):

    if current is None:
        node = Node(int(content[i]), int(content[i+1]))
        i += 2
        nodes.append(node)

        current = node

    elif current.child_length != len(current.children):
        node = Node(int(content[i]), int(content[i+1]))
        i += 2
        nodes.append(node)
        node.parent = current

        current.children.append(node)
        current = node

    elif current.meta is None:
        
        current.meta = []
        for j in range(current.meta_length):
            current.meta.append(int(content[i]))
            i += 1

    else:
        current = current.parent

total = 0
for node in nodes:
    if node.meta:
        total += sum(node.meta)

print(total)
