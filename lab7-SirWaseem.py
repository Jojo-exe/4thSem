def bfs(graph, start_node, goal_node, path=[]):
    visited = set()
    queue = [start_node]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == goal_node:
            return path

        elif node not in visited:
            visited.add(node)
            neighbors = graph[node]

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['C'],
    'E': ['F','H'],
    'F': ['A','B'],
    'G': ['G','F'],
    'H': ['H'],
}

start_node = 'A'
goal_node = 'H'
path = bfs(graph, start_node, goal_node)
print("Optima path To Reacher GoalNode",path)
