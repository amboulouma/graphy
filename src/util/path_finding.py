def shortest_path(initial_vertex, target_vertex, tree):
    if initial_vertex == target_vertex:
        print(initial_vertex, end='')
    elif tree[target_vertex] == None:
        print('There is no possible path between %s and %s' % (initial_vertex, target_vertex))
    else:
        shortest_path(initial_vertex, tree[target_vertex], tree)
        print(' -> %s' % target_vertex, end='')
