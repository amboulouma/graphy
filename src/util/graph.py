import queue as queue

class Graph:

    def __init__(self, graph = {}):
        self.graph = graph


    def show(self):
        predecessors = self.graph.keys()
        for predecessor in sorted(predecessors):
            successors = self.graph[predecessor]
            for successor in sorted(successors):
                print(predecessor + ' -> ' + successor)


    def bfs(self, initial_vertex):
        pi = {}
        state = {}
        q = queue.Queue()
        for vertex in self.graph.keys():
            pi[vertex] = None
            state[vertex] = 'undiscovered'
        q.put(initial_vertex)
        state[initial_vertex] = 'discovered'
        while not(q.empty()):
            vertex_first_out = q.get()
            for successors in self.graph[vertex_first_out]:
                for successor in successors:
                    if state[successor] == 'undiscovered':
                        q.put(successor)
                        state[successor] = 'discovered'
                        pi[successor] = vertex_first_out
            state[vertex_first_out] = 'processed'
        return pi

