from util.graph import Graph

graph = Graph({
    'A' : ['B', 'C'],
    'B' : ['D', 'A'],
    'C' : ['D', 'A'],
    'D' : ['F', 'G', 'B', 'C'],
    'F' : ['D'],
    'G' : ['D']
})

graph.show()