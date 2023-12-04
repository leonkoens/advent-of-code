import re


class Graph:

    def __init__(self):
        self.nodes = {}

    def get_or_create(self, node):
        try:
            node = self.nodes[node]
        except KeyError:
            node = Node(node)
            self.nodes[node.name] = node

        return node

    def resolve(self):
        
        result = []
        zero_edges = []

        node_edges = {node: 0 for node in self.nodes}

        for node in self.nodes:
            for edge in self.nodes[node].edges:
                node_edges[edge.name] += 1

        for d in node_edges:
            if node_edges[d] == 0:
                zero_edges.append(d)

        while zero_edges:

            zero_edges = sorted(zero_edges)

            n = zero_edges.pop(0)
            result.append(n)

            for edge in self.nodes[n].edges:
                node_edges[edge.name] -= 1
                if node_edges[edge.name] == 0:
                    zero_edges.append(edge.name)

        return result


class Node:

    def __init__(self, name):
        self.name = name
        self.edges = []

    def __str__(self):
        return self.name

    def add(self, node):
        self.edges.append(node)
        


graph = Graph()

content = ''
with open('input7.txt') as handle:
    content = handle.read().strip()


regex = re.compile("Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

for line in content.split("\n"):
    match = regex.match(line)

    dep = match.group(1)
    node = match.group(2)

    dep = graph.get_or_create(dep)
    node = graph.get_or_create(node)

    dep.add(node)

order = "".join(graph.resolve())
print(order)
