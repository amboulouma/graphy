import queue as queue

class Graph:

    def __init__(self, graph = {}):
        self.graph = graph


    def __str__(self):
        graph = ''
        predecessors = self.graph.keys()
        for predecessor in sorted(predecessors):
            successors = self.graph[predecessor]
            for successor in sorted(successors):
                graph += predecessor + ' -> ' + successor
                graph += '\n'
        return graph


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
            for successor in self.graph[vertex_first_out]:
                if state[successor] == 'undiscovered':
                    q.put(successor)
                    state[successor] = 'discovered'
                    pi[successor] = vertex_first_out
            state[vertex_first_out] = 'processed'
        return pi


    def dfs(self, initial_vertex):
        pi = {}
        state={}
        stack=[]
        for vertex in self.graph.keys():
            pi[vertex] = None
            state[vertex] = 'undiscovered'
        stack.append(initial_vertex)
        state[initial_vertex]= 'discovered'
        while len(stack):
            current_vertex = stack[-1]
            possible_successor = self.returnUndiscoveredSuccessor(current_vertex, state)
            if possible_successor:
                stack.append(possible_successor)
                state[possible_successor] = 'discovered'
                pi[possible_successor]= current_vertex
            else:
                stack.remove(current_vertex)
                state[current_vertex]='processed'
        return pi
 
 
    def returnUndiscoveredSuccessor(self, current_vertex, state):
        for successor in self.graph[current_vertex]:
            if state[successor] == 'undiscovered':
                return successor
        return None