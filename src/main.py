from util.graph import Graph
from util.showing_functions import *
from util.path_finding import *
import time

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
print(graph)
print()

print()
print('The Breadth-First Search')
start_time = time.time()
show_sorted_traversal(graph.bfs('A'))
print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
print()

print()
print('The shortest path between two vertices')
start_time = time.time()
shortest_path('A', 'E', graph.bfs('A'))
print()
print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
print()

print()
print('The Depth First Search')
start_time = time.time()
show_sorted_traversal(graph.dfs('A'))
print("--- %s milliseconds ---" % ((time.time() - start_time)*1000))
print()

