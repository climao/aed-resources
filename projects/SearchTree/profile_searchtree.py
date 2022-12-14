#
# Profile search tree implementation.
#
# UC: AED
# Author: CJL
# Date: November 2022
#
import searchtree
import profile
import random

atree = None


def setup_tree(n):
    """
    Setup tree to use in tests.

    :param n: Number of elements in tree.
    :return:  None
    """
    global atree

    rlist = random.sample(range(1, n+1), n)
    for i in rlist:
        if atree is None:
            atree = searchtree.SearchTree(i)
        else:
            atree.insert_i(i)


def test_tree(n):
    """
    Test time to find value in tree.
    The test executs a fixed number of operations in a tree
    with n values.

    :param n: Number of elements in tree (not used).
    :return: None
    """
    global atree
    for i in range(100000):
        atree.exists(i)


#
# Test tree imlementation.
# After inserting a random list of values in the tree, we expect search time to be O(lg n).
#
profile.profile_algorithm(test_tree,
                          [100000, 200000, 300000, 400000, 500000],
                          "Árvore Binária - Pesquisa de valores.",
                          use_number_list=False,
                          setup=setup_tree,
                          adjust_for_length=False)
