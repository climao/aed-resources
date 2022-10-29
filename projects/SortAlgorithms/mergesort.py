#
# MergeSort - Python implementation
#
# Author: CJL

def merge(arr, l, m, r):
    """
    Merge two subarrays of arr[]: arr[l..m] and arr[m+1..r].

    :param arr: The array including the 2 sub-arrays to merge.
    :param l: left index
    :param m: middle index
    :param r: right index
    :return: The merged array.
    """
    n1 = m - l + 1
    n2 = r - m

    # Create temporary arrays (stacks) ...
    L = [0] * n1
    R = [0] * n2

    # ... and copy each one form A
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge temporary arrays back to arr[l..r]
    i = 0  # start index of Left subarray
    j = 0  # start index of Right subarray
    k = l  # start index of merged subarray

    # Copy while both temporary arrays have elements, choosing the smallest
    while i < n1 and j < n2:
        if i < n1 and L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    """
    Mergesort algorithm.
    :param arr: The array to sort.
    :param l: left index
    :param r: right index
    :return: The sorted array.
    """
    if l < r:
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


if __name__ == '__main__':
    import random

    LIST_LEN = 30

    arr = random.sample(range(1, LIST_LEN + 1), LIST_LEN)

    print("Unsorted array: ")
    for item in arr:
        print(item, end=" ")

    mergeSort(arr, 0, len(arr) - 1)

    print("\nSorted array: ")
    for item in arr:
        print(item, end=" ")

