from dataclasses import dataclass
import re


content = None
with open('8.txt', 'r') as handle:
    content = [line.strip() for line in handle.readlines()]


@dataclass
class Node:
    name: str

    left: 'Node' = None
    right: 'Node' = None

    def __repr__(self) -> str:
        return self.name


@dataclass
class Resolver:

    current: 'Node'

    def __post_init__(self):
        self.steps = 0
        self.name = self.current.name

    def do_instruction(self, instruction: str) -> bool:
        self.steps += 1

        if instruction == 'L':
            self.current = self.current.left

        elif instruction == 'R':
            self.current = self.current.right

        z_end = self.current.name[-1] == 'Z'

        return z_end


class AdventOfCode:

    def __init__(self, content):
        self.content = content

    def run(self):
        instructions = list(self.content[0])
        roots = []
        nodes = {}

        def get_or_create_node(node_name):

            if node_name in nodes:
                return nodes[node_name]
            
            node = Node(node_name)
            nodes[node_name] = node

            return node

        for line in self.content:
            matches = re.findall('(.+) = \((.+), (.+)\)', line)

            if not matches:
                continue

            node, left, right = matches[0]

            node = get_or_create_node(node)
            left = get_or_create_node(left)
            right = get_or_create_node(right)

            node.left = left
            node.right = right

            if node.name[-1] == 'A':
                roots.append(Resolver(node))

        running = True
        steps = {}

        while running:

            for i in instructions:

                if len(roots) == len(steps):
                    running = False
                    break

                for resolver in roots:
                    done = resolver.do_instruction(i)

                    if done:
                        steps[resolver.name] = resolver.steps
                        resolver.steps = 0
        
        print(steps.values())
        # Python 3.9
        #print(lcm(*list(steps.values())))
                    
        
aoc = AdventOfCode(content)
aoc.run()