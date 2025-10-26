import matplotlib.pyplot as plt
import networkx as nx

node_list = [1, 2, 3]

graph = nx.Graph()
graph.add_nodes_from(node_list)  # Adding multiple nodes at once
graph.add_edges_from([(1, 2), (2, 3), (3, 1)])  # Adding multiple edges at once
print(graph.degree(1))  # Degree of node 1
nx.draw(graph, with_labels=True)

plt.show()
