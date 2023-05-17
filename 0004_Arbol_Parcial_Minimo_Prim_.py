import networkx as nx
import matplotlib.pyplot as plt

def prim(graph):
    # Inicializar el árbol parcial mínimo y el conjunto de nodos visitados
    mst = nx.Graph()
    visited = set()

    # Elegir un nodo inicial aleatorio
    start_node = list(graph.nodes())[0]
    visited.add(start_node)

    while len(visited) != len(graph.nodes()):
        min_weight = float('inf')
        min_edge = None

        # Buscar la arista de peso mínimo que conecta un nodo visitado con uno no visitado
        for node in visited:
            for neighbor, data in graph[node].items():
                if neighbor not in visited and data['weight'] < min_weight:
                    min_weight = data['weight']
                    min_edge = (node, neighbor)

        # Agregar la arista de peso mínimo al árbol parcial mínimo
        if min_edge:
            node1, node2 = min_edge
            mst.add_edge(node1, node2, weight=min_weight)
            visited.add(node2)

    return mst

# Crear el grafo de ejemplo
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=8)
G.add_edge('C', 'E', weight=10)
G.add_edge('D', 'E', weight=2)

# Obtener el árbol parcial mínimo de Prim
mst = prim(G)

# Dibujar el grafo original y el árbol parcial mínimo
plt.figure(figsize=(8, 4))
plt.subplot(121)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.title('Grafo original')

plt.subplot(122)
pos_mst = nx.spring_layout(mst)
nx.draw(mst, pos_mst, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold')
nx.draw_networkx_edge_labels(mst, pos_mst, edge_labels=nx.get_edge_attributes(mst, 'weight'))
plt.title('Árbol Parcial Mínimo de Prim')

plt.tight_layout()
plt.show()
