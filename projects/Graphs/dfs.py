#
# Algoritmo Depth-First Search (DFS)
#
# CJL
# Jan 2023
#

#
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
   # C0  C1  C2  C3  C4  C5  C6 C7
    [ 0,  1,  1,  0,  0,  0,  0, 0], #L0
    [ 1,  0,  0,  1,  0,  0,  0, 0], #L1
    [ 1,  0,  0,  1,  0,  0,  0, 0], #L2
    [ 0,  1,  1,  0,  1,  1,  0, 0], #L3
    [ 0,  0,  0,  1,  0,  1,  1, 0], #L4
    [ 0,  0,  0,  1,  1,  0,  1, 0], #L5
    [ 0,  0,  0,  0,  1,  1,  0, 0], #L6
    [ 0,  0,  0,  0,  0,  0,  0, 0], #L7
]

def add_edge(x, y):
    graph[x][y] = True
    graph[y][x] = True

def dfs(graph, start, visited):
    """

    :param start:  O nó inicial
    :param target: the value to search for
    :return: The node containing the target value or null if it doesn't exist.
    """
    visited.add(start)

    for i in range(len(graph)):
        if i not in visited and graph[start][i]:
            dfs(graph, i, visited)
    return visited


def main():
    add_edge(6, 7)
    print(f"Travessia do grafo usando DFS (inicio=0): {dfs(graph, 0, set())}")


if __name__ == "__main__":
    main()
