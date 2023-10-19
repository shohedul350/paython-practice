# def createGraph():
#     graph = {}
#     # vertices number input form user
#     vertices =  int(input("How many vertices do you want to create?: "))
#     for _ in range(vertices): #input vertex depend on vertices number
#         vertex = input("Enter Vertex: ")
#         neighbors = input("Enter neighbors (comma-separated like A,B or 1,2): ") 
#         if neighbors:
#             graph[vertex] =  neighbors.split(',')
#         else: 
#             graph[vertex] = []
#     return graph
# userGraph = createGraph()
# print(userGraph);

userGraph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# visited = set()
# dfsResult = []
# # DFS function
# def dfs(userGraph, startNode, visited, dfsResult):
#     if startNode not in visited:
#         visited.add(startNode)
#         dfsResult.append(startNode)
#         for neighbor in userGraph[startNode]:
#             dfs(userGraph, neighbor, visited, dfsResult)
# startNode = input("Enter the starting node for DFS: ")
# #call the function
# dfs(userGraph, startNode, visited, dfsResult)
# print(dfsResult) # Print the result

# visited = set()
# # check connection # should return boolean
# def isConnected(userGraph, startNode, targetNode):
#     dfsV2(userGraph, startNode, visited)
#     return targetNode in visited

# def dfsV2(userGraph, node, visited):
#     visited.add(node)
#     for neighbor in userGraph[node]:
#         if neighbor not in visited:
#             dfsV2(userGraph, neighbor, visited)

# startNode = input("Enter the starting node: ")
# targetNode = input("Enter the target node to check connectivity: ")

# connected = isConnected(userGraph, startNode, targetNode)
# if connected:
#     print(f"{startNode} is connected to {targetNode}.")
# else:
#     print(f"{startNode} is not connected to {targetNode}.")

def dfs(graph, start, end, path=[]):
    path = path + [start]
    
    if start == end:
        return path
    
    if start not in graph:
        return None
    
    for node in graph[start]:
        if node not in path:
            new_path = dfs(graph, node, end, path)
            if new_path:
                return new_path
    
    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

source = 'A'
destination = 'F'

result = dfs(graph, source, destination)

if result:
    print(f"Path from {source} to {destination}: {result}")
else:
    print(f"No path found from {source} to {destination}")

