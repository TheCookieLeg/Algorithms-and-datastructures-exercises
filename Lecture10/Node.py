from enum import Enum

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.color = Color.WHITE

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def __repr__(self):
        return f"Node({self.value})"

class Color(Enum):
    WHITE = 1
    GREY = 2
    BLACK = 3