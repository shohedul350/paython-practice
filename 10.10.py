import matplotlib.pyplot as plt
import numpy as np

y = np.array([40, 30, 20, 10])
mylabels = ["Node.js", "Python", "Java", "Php"]

plt.pie(y, labels = mylabels)
plt.show() 


# 

# def create_graph():
#     graph = {}
#     vertices = int(input("Enter the number of vertices: "))
#     for _ in range(vertices):
#         vertex = input("Enter a vertex: ")
#         neighbors = input("Enter neighbors (comma-separated): ")
#         print(neighbors)
#         if neighbors:
#           graph[vertex] = neighbors.split(',')
#     return graph

# user_graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
# print(user_graph)
# # DFS function
# def dfs(user_graph, start_node, visited, dfs_result):
#     if start_node not in visited:
#         visited.add(start_node)
#         dfs_result.append(start_node)
#         for neighbor in user_graph[start_node]:
#             dfs(user_graph, neighbor, visited, dfs_result)

# visited = set()
# dfs_result = []

# # user_graph = create_graph()
# start_node = input("Enter the starting node for DFS: ")
# dfs(user_graph, start_node, visited, dfs_result)
# # Print the result
# print(dfs_result)

# connectivity_visited = set()

# def is_connected(user_graph, start_node, end_node):
  
#     visited_connect_check = set()

#     user_graph_dfs(user_graph, start_node, visited_connect_check)
#     return end_node in visited_connect_check

# def user_graph_dfs(user_graph, node, visited_connect_check):
#     visited_connect_check.add(node)
#     for neighbor in user_graph[node]:
#         if neighbor not in visited_connect_check:
#             user_graph_dfs(user_graph, neighbor, visited_connect_check)


# start_node = input("Enter the starting node: ")
# target_node = input("Enter the target node to check connectivity: ")

# connected = is_connected(user_graph, start_node, target_node)
# if connected:
#     print(f"{start_node} is connected to {target_node}.")
# else:
#     print(f"{start_node} is not connected to {target_node}.")