from dataclasses import dataclass
from functools import reduce
from operator import mul
import re


content = None
with open('8.txt', 'r') as handle:
    content = [line.strip() for line in handle.readlines()]


@dataclass
class Node:
    name: str

    left: 'Node' = None
    right: 'Node' = None


class AdventOfCode:

    def __init__(self, content):
        self.content = content

    def run(self):
        instructions = self.content[0]
        root = None
        nodes = {}

        def get_or_create_node(node_name):
            if node_name in nodes:
                return nodes[node_name]
            
            node = Node(node_name)
            nodes[node_name] = node

            return node

        for line in self.content:

            matches = re.findall('([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)', line)

            if not matches:
                continue

            node, left, right = matches[0]

            node = get_or_create_node(node)
            left = get_or_create_node(left)
            right = get_or_create_node(right)

            node.left = left
            node.right = right

            if node.name == 'AAA':
                root = node

        current = root
        steps = 0

        
        while current.name != 'ZZZ':

            for i in list(instructions):
                if i == 'L':
                    current = current.left
                if i == 'R':
                    current = current.right
                
                steps += 1
        
        
        print(steps)

        
aoc = AdventOfCode(content)
aoc.run()