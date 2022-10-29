#
# Profile binary search algorithm
#
# Author: CJL
#
import profile
import bsearch
import lsearch


def test_bsearch(arr):
    arr = sorted(arr)
    bsearch.binary_search(arr, 0, len(arr)-1, 11000000)


def test_lsearch(arr):
    lsearch.pesquisa_linear_com_sentinela(arr, len(arr), 11000000)



ns = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000]
profile.profile_algorithm(test_bsearch, ns, 'Pesquisa Binária', False, True)
profile.profile_algorithm(test_lsearch, ns, 'Pesquisa Linear', False)