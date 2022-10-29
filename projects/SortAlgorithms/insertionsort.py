#
# Insertion sort - Python implementation
#
# Author: CJL


def insertionsort(A, n):
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


if __name__ == '__main__':
    import random

    LIST_LEN = 30

    arr = random.sample(range(1, LIST_LEN + 1), LIST_LEN)

    print("Unsorted array: ")
    for item in arr:
        print(item, end=" ")

    insertionsort(arr, len(arr))

    print("\nSorted array: ")
    for item in arr:
        print(item, end=" ")