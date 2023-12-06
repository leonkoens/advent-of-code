import string
import re


class Node:

    def __init__(self, child_length, meta_length):
        self.child_length = child_length
        self.meta_length = meta_length

        self.value = 0
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

            if current.child_length > 0:
                try:
                    current.value += current.children[int(content[i]) -1].value
                except IndexError:
                    pass

            i += 1


        if current.child_length == 0:
            current.value = sum(current.meta)

    else:
        current = current.parent

print(nodes[0].value)
