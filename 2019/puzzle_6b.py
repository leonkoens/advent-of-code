import collections


content = None

with open('input_6.txt', 'r') as handle:
    content = handle.readlines()


class Node:

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.path = None

    def __repr__(self):
        return self.name


nodes = dict()

for line in content:

    first, second = line.strip().split(')')

    try:
        first = nodes[first]
    except KeyError:
        first = Node(first)
        nodes[first.name] = first

    try:
        second = nodes[second]
    except KeyError:
        second = Node(second)
        nodes[second.name] = second

    second.parent = first
    first.children.append(second)


queue = collections.deque()
prev_node = None
node = nodes['YOU']

while node.name != 'SAN':
    if node.parent and not node.parent.path:
        node.parent.path = node
        queue.append(node.parent)

    for child in node.children:
        if not child.path:
            child.path = node
            queue.append(child)

    prev_node = node
    node = queue.pop()


total = 0
node = nodes['SAN']

while node.path:
    if node.name == 'YOU':
        break
    node = node.path
    total += 1

print(total-2)

