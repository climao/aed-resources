#
# Selection sort - Python implementation
#
# Author: CJL


def selectionsort(A, n):
    """
    Selection sort algorithm.
    :param A: The array to sort.
    :param n: Length of the array to sort.
    :return: The sorted array.
    """
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]


if __name__ == '__main__':
    import random

    LIST_LEN = 30

    arr = random.sample(range(1, LIST_LEN + 1), LIST_LEN)

    print("Unsorted array: ")
    for item in arr:
        print(item, end=" ")

    selectionsort(arr, len(arr))

    print("\nSorted array: ")
    for item in arr:
        print(item, end=" ")
