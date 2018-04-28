from util.graph import Graph
from util.showing_functions import *

graph = Graph({
    'A' : ['B', 'C'],
    'B' : ['D', 'A'],
    'C' : ['D', 'A'],
    'D' : ['F', 'G', 'B', 'C'],
    'F' : ['D'],
    'G' : ['D']
})

print()
print('The graph')
graph.show()
print()

print()
print('The Breadth-First Search')
show_sorted_traversal(graph.bfs('A'))
print()
