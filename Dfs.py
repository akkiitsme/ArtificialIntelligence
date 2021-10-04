graph={
    '1': ['2', '3'],
    '2': ['4', '5', '1'],
    '3': ['6', '7', '1'],
    '4': ['2'],
    '5': ['6', '2'],
    '6': ['3'],
    '7': ['3']
}

node=input("Enter Path:")
visited = []
stack = []
def Dfs(visited, graph, node):
    visited.append(node)
    stack.append(node)
    while stack:
        s = stack.pop()
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
print("The Traversal is:")
Dfs(visited, graph, node)