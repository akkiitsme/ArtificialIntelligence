graph={
    'A':['B','D','E','C'],
    'B':['F','G'],
    'C':['H'],
    'D':['I'],
    'E':['J','K'],
    'F':['L'],
    'G':['M'],
    'H':['N',],
    'I':['O',],
    'J':['P',],
    'K':['Q',],
    'L':[],
    'M':['R'],
    'N':['S'],
    'O':['T'],
    'P':['U'],
    'Q':[],
    'R':[],
    'S':[],
    'T':[],
    'U':[]
}
Traversal=[]
visited=[]
queue=[]
def Bfs(graph,start,target,path):
    queue.append(start)
    while queue:
        s=queue.pop(0)
        path.append(s)
        visited.append(s)
        if s==target:
            return path
        for neighbour in graph[s]:
            if neighbour not in visited:
                queue.append(neighbour)
print("The four queen path is:")
Traversal=Bfs(graph,'A','S',Traversal)
print(Traversal)                


