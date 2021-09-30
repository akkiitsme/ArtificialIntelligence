graph = {
    '1': ['2', '3'],
    '2': ['4', '5', '1'],
    '3': ['6', '7', '1'],
    '4': ['2'],
    '5': ['6', '2'],
    '6': ['3'],
    '7': ['3']
}
visited = []
queue = []
def Bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("The Traversal is:")
Bfs(visited, graph, '2')
