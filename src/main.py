from util.graph import Graph
from util.showing_functions import *
from util.path_finding import *


graph = Graph({
    'A' : ['B', 'C'],
    'B' : ['D', 'A'],
    'C' : ['D', 'A'],
    'D' : ['E', 'F', 'B', 'C'],
    'E' : ['D'],
    'F' : ['D']
})

print()
print('The graph')
graph.show()
print()

print()
print('The Breadth-First Search')
show_sorted_traversal(graph.bfs('A'))
print()
shortest_path('A', 'E', graph.bfs('A'))
print()
