
from collections import deque
# Default Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

#print function
def printPath(path):
    for i in range(len(path)):
        print(path[i], end=",")
    print()

# find paths function
def findPaths(graph, start, end):
    q = deque()    
    path = [start] 
    q.append([start])
  
    while q:
        path = q.popleft()
        last = path[-1]
        if last == end:  
            printPath(path)
        for neighbor in graph[last]:
            if neighbor not in path:
                newPath = path.copy()
                newPath.append(neighbor)
                q.append(newPath)
# call function
findPaths(graph, "A", "F")

# connecting check function
def areConnected(graph, start, end):
    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)

    while q:
        current = q.popleft()

        if current == end:
            return True 

        for neighbor in graph[current]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

    return False 
# call function
print(areConnected(graph, "A", "F"))


