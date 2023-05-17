import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo de ejemplo
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=8)
G.add_edge('C', 'E', weight=10)
G.add_edge('D', 'E', weight=2)

# Aplicar Kruskal para obtener el árbol de expansión mínima
mst = nx.minimum_spanning_tree(G)

# Dibujar el grafo original
pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, font_weight='bold', width=1.5)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)

# Dibujar el árbol de expansión mínima
nx.draw_networkx_edges(mst, pos, edge_color='red', width=2)

# Mostrar el gráfico
plt.axis('off')
plt.show()

