#
# Binary search - Python implementation
#
# Author: CJL

def binary_search(A, p, u, x):
    """
    Binary search algorithm.
    :param A: The array to search.
    :param p: The first index in the array.
    :param u: The last index in the array.
    :param x: The value beeing searched.
    :return: The first index where x exists in the array, or -1 if x doesn't exist in the array.
    """
    while p <= u:
        m = (p + u) // 2
        if A[m] == x:
            return m
        elif A[m] > x:
            u = m - 1
        else:
            p = m + 1
    return -1


def binary_search_r(A, p, u, x):
    """
    Binary search algorithm.
    :param A: The array to search.
    :param p: The first index in the array.
    :param u: The last index in the array.
    :param x: The value beeing searched.
    :return: The first index where x exists in the array, or -1 if x doesn't exist in the array.
    """
    if (p > u):
        return -1
    else:
        m = (p + u) // 2
        if A[m] == x:
            return m
        elif A[m] > x:
            binary_search_r(A, p, m-1, x)
        else:
            binary_search_r(A, m+1, u, x)


if __name__ == '__main__':
    import random

    LIST_LEN = 2000000

    arr = random.sample(range(1, LIST_LEN + 1), LIST_LEN)
    sorted_arr = sorted(arr)

    valor = 33
    if binary_search(sorted_arr, 0, len(sorted_arr) - 1, valor) != -1:
        print(f"Valor {valor} foi encontrado")
    else:
        print(f"Valor {valor} NÃO foi encontrado")