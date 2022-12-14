#
# Teste dos tempos de execução de vários algoritmos
# sobre árvores de pesquisa.
#
# UC: AED
# Author: CJL
# Date: November 2022
#
import searchtree
import profile
import random

atree = None


def setup_random_tree(n):
    global atree

    atree = None

    # Gerar uma lista aleatória de números entre 1 e n.
    rlist = random.sample(range(1, n+1), n)

    # Inserir a lista na árvore.
    for item in rlist:
        if atree is None:
            atree = searchtree.SearchTree(item)
        else:
            atree.insert_i(item)


def setup_ordered_tree(n):
    global atree

    atree = None

    # Gerar uma lista ordenada de números entre 1 e n.
    olist = list(range(1, n+1))

    # Inserir a lista na árvore.
    for item in olist:
        if atree is None:
            atree = searchtree.SearchTree(item)
        else:
            atree.insert_i(item)


def test_tree(n):
    global atree

    for i in range(1, 10000):
        atree.exists_i(n)


profile.profile_algorithm(test_tree,
                          [100000, 200000, 300000, 400000, 500000],
                          "Árvores de Pesquisa Binária - Pesquisa em árvore com valores aleatórios.",
                          use_number_list=False,
                          setup=setup_random_tree,
                          adjust_for_length=False)

profile.profile_algorithm(test_tree,
                          [10000, 20000, 30000, 40000, 50000],
                          "Árvores de Pesquisa Binária - Pesquisa em árvore com valores ordenados.",
                          use_number_list=False,
                          setup=setup_ordered_tree,
                          adjust_for_length=False)
