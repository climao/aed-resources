#
# Algoritmos de pesquisa linear.
#
# UC: Algoritmos e estruturas de dados.
# Autor: Carlos Limão
# Data: 22/10/2023
#

def pesquisa_linear(A, n, x):
    """
    O algoritmo Pesquisa-Linear, tal como estudado na aula teórica.

    :param A: Um array.
    :param n: O número de elementos no array.
    :param x: O valor a procurar no array.
    :return: A posição do valor procurado no array, ou -1 caso esse valor não exista no array.
    """
    result = -1
    for i in range(n):
        if A[i] == x:
            result = i
    return result


def pesquisa_linear_melhorada(A, n, x):
    """
    O algoritmo Pesquisa-Linear-Melhorada, tal como estudado na aula teórica.

    :param A: Um array.
    :param n: O número de elementos no array.
    :param x: O valor a procurar no array.
    :return: A posição do valor procurado no array, ou -1 caso esse valor não exista no array.
    """
    result = -1
    for i in range(n):
        if A[i] == x:
            return i
    return result


def pesquisa_linear_com_sentinela(A, n, x):
    """
    O algoritmo Pesquisa-Linear-Com-Sentinela, tal como estudado na aula teórica.

    :param A: Um array.
    :param n: O número de elementos no array.
    :param x: O valor a procurar no array.
    :return: A posição do valor procurado no array, ou -1 caso esse valor não exista no array.
    """
    last_item = A[-1]
    A[-1] = x
    i = 1
    while A[i] != x:
        i = i + 1
    A[-1] = last_item
    if i < n - 1 or A[-1] == x:
        return i
    else:
        return -1
