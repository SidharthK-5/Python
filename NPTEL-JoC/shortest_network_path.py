import matplotlib.pyplot as plt
import networkx as nx

graph = nx.read_edgelist(
    "data/weighted_edgelist.txt", nodetype=int, data=(("weight", float),)
)
print("Nodes in the weighted graph:")
print(graph.nodes())
print("Edges in the weighted graph with weights:")
for u, v, weight in graph.edges(data="weight"):
    print(f"({u}, {v}) with weight {weight}")
# Compute shortest path using Dijkstra's algorithm
source_node = 1
target_node = 4
shortest_path = nx.dijkstra_path(
    graph, source=source_node, target=target_node, weight="weight"
)
print(f"Shortest path from node {source_node} to node {target_node}: {shortest_path}")
# Compute the length of the shortest path
path_length = nx.dijkstra_path_length(
    graph, source=source_node, target=target_node, weight="weight"
)
print(f"Length of the shortest path: {path_length}")
# Visualize the graph


pos = nx.spring_layout(graph)
edge_labels = nx.get_edge_attributes(graph, "weight")
nx.draw(
    graph, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10
)
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
plt.show()
# Save the graph to a file
nx.write_gexf(graph, "data/weighted_graph.gexf")
