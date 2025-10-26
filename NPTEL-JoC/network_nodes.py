import matplotlib.pyplot as plt
import networkx as nx

# Initialize a graph
G = nx.Graph()

# Add nodes to graph
G.add_node(1, label="Node 1")
G.add_node(2, label="Node 2")
G.add_node(3, label="Node 3")

# Add edges between nodes
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# Print nodes and edges
print("Nodes in the graph:")
print(G.nodes(data=True))
print("Edges in the graph:")
print(G.edges(data=True))

nx.draw(G, with_labels=True)
plt.show()
