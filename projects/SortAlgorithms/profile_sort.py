#
# Profile sorting algorithms
#
# Author: CJL
#
import profile
import selectionsort
import insertionsort
import mergesort
import quicksort


def test_selectionsort(arr):
    selectionsort.selectionsort(arr, len(arr))


def test_insertionsort(arr):
    insertionsort.insertionsort(arr, len(arr))


def test_mergesort(arr):
    mergesort.mergeSort(arr, 0, len(arr) - 1)


def test_quicksort(arr):
    quicksort.quicksort(arr, 0, len(arr) - 1)


ns = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
#profile.profile_algorithm(test_selectionsort, ns, 'Selection Sort', False, )
#profile.profile_algorithm(test_insertionsort, ns, 'Insertion Sort', False, )
#profile.profile_algorithm(test_mergesort, ns, 'Merge Sort', False, )
profile.profile_algorithm(test_quicksort, ns, 'Quicksort', False)