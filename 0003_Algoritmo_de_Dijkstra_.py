import sys
import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(G, start, end):
    # Inicializar el diccionario de distancias
    distances = {vertex: sys.maxsize for vertex in G}
    distances[start] = 0

    # Inicializar la cola de prioridad
    pq = [(0, start)]

    # Inicializar el diccionario de padres
    parents = {vertex: None for vertex in G}

    # Implementar el algoritmo de Dijkstra
    while pq:
        # Obtener el vértice con la distancia más corta
        (current_distance, current_vertex) = heapq.heappop(pq)

        # Si ya visitamos el vértice de destino, salir del bucle
        if current_vertex == end:
            break

        # Si la distancia actual es mayor que la distancia almacenada,
        # ignorar este vértice
        if current_distance > distances[current_vertex]:
            continue

        # Iterar por los vértices adyacentes
        for neighbor, weight in G[current_vertex].items():
            distance = current_distance + G[current_vertex][neighbor]['weight']


            # Si la distancia es más corta que la almacenada, actualizar
            # la distancia y el padre
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    # Devolver la distancia y el camino más corto
    path = []
    while end is not None:
        path.append(end)
        end = parents[end]
    path.reverse()

    return distances, path

# Crear un grafo
G = nx.Graph()
G.add_edge('A', 'B', weight=3)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=2)
G.add_edge('C', 'D', weight=5)

# Visualizar el grafo
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=15)
plt.axis('off')
plt.show()

# Ejecutar el algoritmo de Dijkstra
distances, path = dijkstra(G, 'A', 'D')

# Mostrar la distancia y el camino más corto
print('Distancia más corta:', distances['D'])
print('Camino más corto:', path)

