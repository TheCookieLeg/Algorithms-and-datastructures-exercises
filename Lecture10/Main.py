from queue import Queue
from Graph import Graph
from Node import Node

graph = Graph()

graph.add_node('r') #0
graph.add_node('s') #1
graph.add_node('t') #2
graph.add_node('u') #3
graph.add_node('v') #4
graph.add_node('w') #5
graph.add_node('x') #6
graph.add_node('y') #7

graph.add_edge('r','s')
graph.add_edge('r', 'v')
graph.add_edge('s', 'w')
graph.add_edge('w', 't')
graph.add_edge('w','x')
graph.add_edge('x','y')
graph.add_edge('x','u')
graph.add_edge('x','t')
graph.add_edge('t','u')
graph.add_edge('u','y')

print(graph)