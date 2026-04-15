from Node import Node

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)
        return self.nodes[value]

    def add_edge(self, value1, value2, bidirectional=True):
        node1 = self.add_node(value1)
        node2 = self.add_node(value2)

        node1.add_neighbor(node2)
        if bidirectional:
            node2.add_neighbor(node1)

    def __repr__(self):
        return "\n".join(
            f"{node.value}: {[n.value for n in node.neighbors]}"
            for node in self.nodes.values()
        )