#
# Algoritmo de Dijkstra implementado usando uma lista de adjacencias.
#
# CJL
# jan 2023
#
import math

#
# Um grafo, descrito como uma lista de adjacencias.
#
#                 +---+              +---+
#                 | 1 |              | 5 |
#             2 / +---+ \ 5     15 / +---+ \ 6
#             /           \      /     |     \
#       +---+              +---+       |       +---+
#       | 0 |              | 3 |     6 |       | 6 |
#       +---+              +---+       |       +---+
#            \           /       \     |     /          +---+
#            6 \ +---+ / 8      10 \ +---+ / 2          | 7 |
#                | 2 |               | 4 |              +---+
#                +---+               +---+
#
# O grafo é um dicionário. Elimina a necessidade de armazenar zeros para descrever ligações não existentes.
# As chaves são as designações dos nós.
# Os valores são uma lista de pares (listas) que descrevem nós vizinhos e respetiva distância.
#
graph = {
    0: [[1, 2], [2, 6]],
    1: [[0, 2], [3, 5]],
    2: [[0, 6], [3, 8]],
    3: [[1, 5], [2, 8], [5, 15], [4, 10]],
    4: [[3, 10], [6, 2]],
    5: [[3, 15], [6, 6]],
    6: [[5, 6], [4, 2]],
    7: []
}

#
# Análise temporal, admitindo que V é o nº de vértices e E é o nº de arestas:
#    1) Escolher o nó com a distância mínima de entre os não-visitados, requer O(V), pois temos de verificar todos.
#    2) Para cada vertice selecionado antes, temos de atualizar os vizinhos para ter em consideração o novo caminho.
#       a) Cada vizinho pode ser atualizado em O(1).
#       b) No máximo cada vértice tem V-1 vizinhos
#       c) Para atualizar todos os vizinhos precisamos de O(V) * O(1) = O(V)
#    3) O tempo para visitar todos os vértices é O(|V)
#    4) A complexidade temporal total é, portanto, O(|V|) x (O(|V|) + O(|V|)) = O(|V|^2)
#
# Apesar desta implementação ser mais eficiente que a que utiliza uma matriz de adjacencias, é também O(V^2).
#
def dijkstra(graph, start):
    """
    Calcula as distâncias mais curtas entre o nó "start" e os restantes nós no grafo.

    :param graph: O grafo descrito como uma lista de adjacencias.
    :param start: Nome do nó inicial (0 a n-1).
    :return: Dicionário com as distâncias claculadas. Cada entrada tem distância do nó inicial ao nó descrito pela chave.
    """
    distances = {k: math.inf for k in graph.keys()}  # Usar um dicionário para as distâncias.
    visited = set()
    distances[start] = 0

    for _ in range(len(graph)):

        # Encontrar o nó que atualmente está mais próximo do nó inicial (start)...
        shortest_distance = math.inf
        min_node = None
        for i in graph.keys():
            # ... selecionando-o a partir dos nós que ainda não foram visitados.
            if i not in visited and distances[i] < shortest_distance:
                shortest_distance = distances[i]
                min_node = i

        if min_node is None:
            continue            # Não há mais nós acessíveis

        visited.add(min_node)

        # Para todos os vizinhos, atualizar o caminho mais curto.
        for node, weight in graph[min_node]:
            if node not in visited and distances[node] > distances[min_node] + weight:
                distances[node] = distances[min_node] + weight

    return distances


def get_shortest_path(start, stop, graph, distances):
    """
    Devolve o caminho mais curto entre os nós start e stop.

    :param start: Índice do nó de partida.
    :param stop:  Índice do nó de chegada.
    :param distances: lista com as distâncias mais curtas entre o nó start e todos os outros nós.
    :return: lista de nós pela ordem correspondente ao caminho mais curto.
    """
    path = []
    path.insert(0, stop)
    while path[0] != start:
        shortest_distance = math.inf
        shortest_index = -1
        for node, weight in graph[path[0]]:
            if distances[node] < shortest_distance:
                shortest_distance = distances[node]
                shortest_index = node
        if shortest_index == -1:
            return []   # Não há caminho entre a origem e o destino!
        path.insert(0, shortest_index)
    return path


def main():
    start = 0
    distances = dijkstra(graph, start)
    print(f"Distâncias a partir do nó {start}: {distances}")
    for i in graph.keys():
        print(f"Caminho {start} -> {i}: {get_shortest_path(start, i, graph, distances)} ({distances[i]})")
        pass


if __name__ == "__main__":
        main()
