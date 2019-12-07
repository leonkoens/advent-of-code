
def log(msg):
    print(msg)

content = None

with open('input_6.txt', 'r') as handle:
    content = handle.readlines()


class Node:

    def __init__(self, name):
        self.name = name
        self.parent = None

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


total = 0
for key in nodes:
    node = nodes[key]
    parent = node.parent

    while parent is not None:
        total += 1
        parent = parent.parent

print(total)

