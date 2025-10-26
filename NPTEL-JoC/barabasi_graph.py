import matplotlib.pyplot as plt
import networkx as nx

graph = nx.barabasi_albert_graph(
    10, 2
)  # 10 nodes, each new node attaches to 2 existing nodes
print("Nodes in the Barabási–Albert graph:")
print(graph.nodes())
print("Edges in the Barabási–Albert graph:")
print(graph.edges())
nx.draw(graph, with_labels=True)
plt.show()

# Save the graph to a file
nx.write_gexf(graph, "data/barabasi_albert_graph.gexf")
