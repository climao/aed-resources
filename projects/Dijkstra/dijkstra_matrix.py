#
# Algoritmo de Dijkstra implementado usando uma matriz de adjacencias.
#
# CJL
# jan 2023
#
import math

#
# Um grafo, descrito como uma matriz de adjacencias.
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
# Cada posição (x,y) na matriz representa o custo do trajeto x -> y.
# Para um grafo não dirigido (x,y)=(y,x) (a matriz é simétrica).
#
graph = [
    [0,  2,  6,  0,  0,  0,  0, 0],
    [2,  0,  0,  5,  0,  0,  0, 0],
    [6,  0,  0,  8,  0,  0,  0, 0],
    [0,  5,  8,  0, 10, 15,  0, 0],
    [0,  0,  0, 10,  0,  6,  2, 0],
    [0,  0,  0, 15,  6,  0,  6, 0],
    [0,  0,  0,  0,  2,  6,  0, 0],
    [0,  0,  0,  0,  0,  0,  0, 0],
]

def add_edge(x, y, cost):
    pass

def add_vertex(v):
    pass

#
# Análise temporal, admitindo que V é o nº de vértices e E é o nº de arestas:
#    1) Escolher o nó com a distância mínima de entre os não-visitados, requer O(V), pois temos de verificar todos.
#    2) Para cada vertice selecionado antes, temos de atualizar os vizinhos para ter em consideração o novo caminho.
#       a) Cada vizinho pode ser atualizado em O(1).
#       b) No máximo cada vértice tem V-1 vizinhos
#       c) Para atualizar todos os vizinhos precisamos de O(V) * O(1) = O(V)
#    3) O tempo para visitar todos os vértices é O(V)
#    4) A complexidade temporal total é, portanto, O(V) x (O(V) + O(V)) = O(V^2)
#
# Este tempo pode parecer muito elevado, mas é melhor que usar força-bruta que seria O((V-1)!)
#
def dijkstra(graph, start):
    """
    Calcula as distâncias mais curtas entre o nó "start" e os restantes nós no grafo.

    :param graph: O grafo descrito como uma matriz de adjacencias.
    :param start: Índice do nó inicial (0 a n-1).
    :return: array de distâncias claculadas. Cada posição i tem distância do nó inicial ao nó i.
    """
    distances = [math.inf] * len(graph)
    distances[start] = 0
    visited = set()

    for _ in range(len(graph)):

        # Encontrar o nó que atualmente está mais próximo do nó inicial (start)...
        shortest_distance = math.inf
        min_node = -1
        for i in range(len(graph)):
            # ... selecionando-o a partir dos nós que ainda não foram visitados.
            if i not in visited and distances[i] < shortest_distance:
                shortest_distance = distances[i]
                min_node = i

        if min_node == -1:
            continue        # Não há mais nós acessíveis
        else:
            #print("Visitando nó " + str(min_node) + " à distância " + str(shortest_distance) + " do nó " + str(start))
            pass

        # Marcar este nó como visitado.
        visited.add(min_node)

        # ... agora, para todos os nós vizinhos deste,...
        for i in range(len(graph[min_node])):
            # ... se o caminho ao longo dessa aresta é mais curto...
            if i not in visited and graph[min_node][i] != 0 and distances[i] > distances[min_node] + graph[min_node][i]:
                # ...salvar este caminho como sendo o caminho mais curto.
                distances[i] = distances[min_node] + graph[min_node][i]
                # print("A atualizar distância do nó " + str(i) + " para " + str(distance[i]))

        # print("Nós visitados: " + str(visited))
        # print("Atuais distâncias mais curtas: " + str(distance))

    return distances

def get_shortest_path(start, stop, graph, distances):
    """
    Devolve o caminho mais curto entre os nós start e stop.

    :param start: Índice do nó de partida.
    :param stop:  Índice do nó de chegada.
    :param distances: lista com as distâncias mais curtas entre o nó start e todos os outros nós.
    :return:
    """
    path = []
    path.insert(0, stop)
    while path[0] != start:
        shortest_distance = math.inf
        min_node = -1
        for i in range(len(graph)):
            if graph[path[0]][i] and distances[i] < shortest_distance:
                shortest_distance = distances[i]
                min_node = i
        if min_node == -1:
            return []   # Não há caminho entre a origem e o destino!
        path.insert(0, min_node)
    return path


def main():
    start = 0
    distances = dijkstra(graph, start)
    print(f"Distâncias a partir do nó {start}: {distances}")
    for i in range(len(graph)):
        print(f"Caminho {start} -> {i}: {get_shortest_path(start, i, graph, distances)} ({distances[i]})")


if __name__ == "__main__":
        main()
  
