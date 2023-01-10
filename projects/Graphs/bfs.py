#
# Algoritmo Breadth-First-Search (BFS)
#
# CJL
# Jan 2023

# Um grafo, descrito como uma matriz de adjacencias.
#
#                 +---+              +---+
#                 | 1 |              | 5 |
#               / +---+ \         / +---+ \
#             /           \      /     |     \
#       +---+              +---+       |       +---+
#       | 0 |              | 3 |       |       | 6 |
#       +---+              +---+       |       +---+
#            \           /       \     |     /          +---+
#              \ +---+ /           \ +---+ /            | 7 |
#                | 2 |               | 4 |              +---+
#                +---+               +---+
#
# Cada posição (x,y) na matriz representa o facto de haver ou não ligação entre x e y.
# Para um grafo não dirigido (x,y)=(y,x) (a matriz é simétrica).
#
graph = [
    [0,  1,  1,  0,  0,  0,  0, 0],
    [1,  0,  0,  1,  0,  0,  0, 0],
    [1,  0,  0,  1,  0,  0,  0, 0],
    [0,  1,  1,  0,  1,  1,  0, 0],
    [0,  0,  0,  1,  0,  1,  1, 0],
    [0,  0,  0,  1,  1,  0,  1, 0],
    [0,  0,  0,  0,  1,  1,  0, 0],
    [0,  0,  0,  0,  0,  0,  0, 0],
]

def distance_bfs(graph, start):
    """
    Algoritmo Breadth-First-Search (BFS)

    :param graph: grafo na forma de uma matriz de adjacencias. Cada posição (x,y) é 1 se existir uma aresta entre os 2.
    :param start: the node to start from.
    :return: array containing the shortest distances from the given start node to each other node
    """
    # Uma fila para guardar nós a visitar. Inicialmente o nó inicial.
    queue = [start]

    # Conjunto de nós visitados. Inicialmente "start". O(1)
    visited = set((start,))

    # A distãncia de "start" a sí próprio é zero.
    # Não são necessárias outras inicializaçoes, pois BFS visita cada nó exatamente uma vez.
    distances = [float("inf")] * len(graph)

    # Enquanto existirem nós na fila...
    while len(queue) > 0:
        #print("Nós visitados: " + str(visited))
        #print("Distâncias: " + str(distances))
        node = queue.pop(0)
        #print("Vai remover nó " + str(node) + " da fila...")
        # ...par todos os vizinhos ainda não visitados....
        for i in range(len(graph[node])):
            if graph[node][i] and i not in visited:
                # ...marcar como visitado, atualizar distância e colocar na fila.
                visited.add(i)
                distances[i] = distances[node] + 1
                queue.append(i)
                #print("A visitar nó " + str(i) + ", com distância " + str(distances[i]) + " e colocá-lo na fila")

    return distances


def bfs(graph, start):
    """
    Algoritmo Breadth-First-Search (BFS)

    :param graph: grafo na forma de uma matriz de adjacencias. Cada posição (x,y) é 1 se existir uma aresta entre os 2.
    :param start: the node to start from.
    :return: array containing the shortest distances from the given start node to each other node
    """
    # Uma fila para guardar nós a visitar. Inicialmente o nó inicial.
    queue = [start]

    # Conjunto de nós visitados. Inicialmente "start". O(1)
    visited = set((start,))

    # Não são necessárias outras inicializaçoes, pois BFS visita cada nó exatamente uma vez.
    visits = []

    # Enquanto existirem nós na fila...
    while len(queue) > 0:
        node = queue.pop(0)
        for i in range(len(graph[node])):
            if graph[node][i] and i not in visited:
                # ...marcar como visitado e colocar na fila.
                visited.add(i)
                queue.append(i)

    return visited


def main():
    start = 7
    print(f"Travessia do grafo usando BFS (início={start}): {bfs(graph, start)}")
    print(f"Distâncias a partir do nó {start} usando BFS: {distance_bfs(graph, start)}")


if __name__ == "__main__":
    main()
