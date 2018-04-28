class Graph:

    def __init__(self, graph = {}):
        self.graph = graph


    def show(self):
        predecessors = self.graph.keys()
        for predecessor in sorted(predecessors):
            successors = self.graph[predecessor]
            for successor in sorted(successors):
                print(predecessor + ' -> ' + successor)

    def bfs(self, vertex):
        pi = {}
        
        return pi