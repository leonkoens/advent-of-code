import re


content = None
with open(__file__.replace('.py', '.txt'), 'r') as handle:
    content = handle.readlines()

#content = """
#$ cd /
#$ ls
#dir a
#14848514 b.txt
#8504156 c.dat
#dir d
#$ cd a
#$ ls
#dir e
#29116 f
#2557 g
#62596 h.lst
#$ cd e
#$ ls
#584 i
#$ cd ..
#$ cd ..
#$ cd d
#$ ls
#4060174 j
#8033020 d.log
#5626152 d.ext
#7214296 k
#""".strip().split("\n")


class Node:
    
    def __init__(self, name, parent: 'Node' = None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.total_size = 0

    def __repr__(self):
        return f'[Node {self.name} ({self.total_size})]'

    

root = None
current = None


for line in content:
    line = line.strip()

    if not root and line == '$ cd /':
        root = Node(name='/')
        current = root

    elif line == '$ cd /':
        current = root

    elif line == '$ ls':
        continue
    elif line.startswith('$ cd'):
        to = line.split(' ')[2]

        if to == '..':
            current = current.parent
        else:
            current = current.children[to]

    else:
        size, name = line.split(' ')

        if name in current.children:
            continue

        current.children[name] = Node(name=name, parent=current)

        if size != 'dir':

            current.children[name].total_size = int(size)

            parent = current
            while parent is not None:
                parent.total_size += int(size)
                parent = parent.parent

unused = 70000000 - root.total_size
needed = 30000000 - unused
needed_smallest_dir = 70000000

def calculate(node, indent):
    global needed, needed_smallest_dir  # noqa :')

    #print(' ' * indent, node)
    size = 0

    if len(node.children) > 0:
        
        for child in node.children.values():
            size += calculate(child, indent+2)

        if node.total_size <= 100000:
            size += node.total_size 

        if needed and node.total_size >= needed:
            needed_smallest_dir = min(needed_smallest_dir, node.total_size)
            
    return size

print("Part 1", calculate(root, 0))
print("Part 2", needed_smallest_dir)

