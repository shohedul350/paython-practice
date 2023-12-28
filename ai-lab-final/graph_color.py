import networkx as nx
import matplotlib.pyplot as plt


def is_valid(graph, coloring):
    for U, V in graph.edges():
        if coloring[U] == coloring[V]:
            return False
    return True

def greedy_coloring(graph):
  colors = ['Red', 'Green', 'Blue', 'Yellow', 'Purple']
  coloring = {}
  for node in graph.nodes():
      adjacent_colors = {coloring.get(neighbor) for neighbor in graph.neighbors(node)}
      coloring[node] = next((color for color in colors if color not in adjacent_colors), 'Red')
  return coloring

# graph
G = nx.Graph()
# G.add_edges_from([('WA', 'NT'), ('WA', 'SA'), ('B', 'C'), ('B', 'F'), ('C', 'D'), ('C', 'F'), ('D', 'E'), ('D', 'F'), ('E', 'F')])

G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (4, 6), (5, 6)])

coloring_result = greedy_coloring(G)
print('Coloring:', coloring_result)
print('Valid:', is_valid(G, coloring_result) )

node_color_list = [coloring_result[node] for node in G.nodes()]

# Draw the graph with colors
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True,  node_color=node_color_list)
plt.show()