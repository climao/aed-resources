#
# Quicksort - Python implementation
#
# Author: CJL

def partition(A, p, u):
    """
    Performs partion step for quiksort algorithm.
    :param A: The array with the range to partition.
    :param p: Start index.
    :param u: End index.
    :return: The pivot position.
    """
    q = p
    for i in range(p, u):
        if A[i] <= A[u]:
            A[q], A[i] = A[i], A[q]
            q += 1
    A[q], A[u] = A[u], A[q]
    return q

def quicksort(A, p, u):
    """
    Quicksort algortihm.
    :param A: The array containing the elements to sort.
    :param p: The first index of the array to sort.
    :param u: The last index of the array to sort.
    :return: Nothing.
    """
    if p >= u:
        return
    m = partition(A, p, u)
    quicksort(A, p, m - 1)
    quicksort(A, m + 1, u)


def quicksortIterative(arr, l, h):
    """
    An iterative version of the quicksort algorithm.
    :param arr: The array containing the elements to sort.
    :param l:
    :param h:
    :return:
    """
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, l, h)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


if __name__ == '__main__':
    import random

    LIST_LEN = 30

    arr = random.sample(range(1, LIST_LEN + 1), LIST_LEN)

    print("Unsorted array: ")
    for item in arr:
        print(item, end=" ")

    quicksort(arr, 0, len(arr) - 1)

    print("\nSorted array: ")
    for item in arr:
        print(item, end=" ")
