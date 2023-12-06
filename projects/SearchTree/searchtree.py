#
# Search tree.
#
# UC: AED
# Author: CJL
# Date: November 2022
#

class SearchTree:

    def __init__(self, data=None, left=None, right=None):
        """
        Construtor de uma árvore binária.

        :param data: valor a armazenar no nó.
        :param left: o nó seguinte à esquerda. None se não existir.
        :param right: o nó seguinte à direita. None se não existir.
        """
        self.data = data
        self.left = left
        self.right = right

    def depth(self):
        """
        Calcula a profundidade da árvore (profundidade do nó mais profundo).

        :return: -1 se a árvore não tem nós
                  0 se a árvore apens tem a raiz
                  n - o número de segmentos entre a raiz e a folha mais profunda.
        """
        if self.data is None:
            return -1

        if self.left is None and self.right is None:
            return 0

        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0

        return max(left_depth, right_depth) + 1

    def insert_left(self, data):
        """
        Insere nó á esquerda.

        :param data: Valor a guardar no novo nó.
        :return: None
        """
        self.left = SearchTree(data)
        return self

    def insert_right(self, data):
        """
        Insere nó á direita.

        :param data: Dados a guardar no novo nó.
        :return: None
        """
        self.right = SearchTree(data)
        return self

    def insert(self, data):
        """
        Insere, recursivamente, valor especificado na posição correta da árvore.

        :param data: valor a adicionar à árvore.
        :return:  None
        """
        if not self.data:
            self.data = data
            return

        if self.data == data:
            return              # Entrada duplicada. Sai sem fazer nada.
        elif data < self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left = SearchTree(data)
            return
        else:
            if self.right:
                self.right.insert(data)
                return
            self.right = SearchTree(data)

    def insert_i(self, data):
        """
        Insere, iterativamente, o valor especificado na posição correta da árvore.

        :param data: valor a adicionar à árvore.
        :return:  None
        """
        found = False
        p = self
        q = None
        while p is not None and not found:
            q = p
            if p.data == data:
                found = True
            elif p.data > data:
                p = p.left
            else:
                p = p.right

        if found:
            return      # Entrada duplicada. Sai sem fazer nada.

        if q.data > data:
            q.insert_left(data)
        else:
            q.insert_right(data)

    def delete(self, data):
        """
        Remove da árvore o nó com o valor especificado.

        :param data: valor a remover.
        :return: A nova raiz d árvore, possivelmente diferente da inicial, depois da remoção.
        """
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
            return self
        if data > self.data:
            if self.right:
                self.right = self.right.delete(data)
            return self

        # Este nó tem o valor procurado e não é um nó completo!
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right

        # O nó que tem o valor a apagar é um nó completo.
        min_node_of_larger = self.right
        while min_node_of_larger.left:
            min_node_of_larger = min_node_of_larger.left
        self.data = min_node_of_larger.data                         # substitui valor pelo mínimo dos maiores
        self.right = self.right.delete(min_node_of_larger.data)     # Apaga nó com mínimo copiado

        return self

    def min(self):
        """
        Devolve o menor valor armazenado na árvore.

        :return: Menor valor na árvore.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current.data

    def max(self):
        """
        Devolve o maior valor armazenado na árvore.

        :return: Maior valor na árvore.
        """
        current = self
        while current.right is not None:
            current = current.right
        return current.data

    def exists(self, data):
        """
        Avalia, recursivamente, a existência na árvore do valor especificado.

        :param data: Valor a procurar.
        :return: True se valor existe na árvore.
                 False se valor não existe na árvore.
        """
        if data == self.data:
            return True
        elif data < self.data:
            if self.left is None:
                return False
            return self.left.exists(data)
        else:
            if self.right is None:
                return False
            return self.right.exists(data)

    def exists_i(self, data):
        """
        Avalia, iterativamente, a existência na árvore do valor especificado.

        :param data: Valor a procurar.
        :return: True se valor existe na árvore.
                 False se valor não existe na árvore.
        """
        found = False
        p = self

        while p is not None and not found:
            if p.data == data:
                found = True
            elif p.data > data:
                p = p.left
            else:
                p = p.right

        return found

    def get_node(self, data):
        found = False
        p = self
        q = None

        while p is not None and not found:
            q = p
            if p.data == data:
                found = True
            elif p.data > data:
                p = p.left
            else:
                p = p.right

        if found:
            return q
        else:
            return None

    def traverse_tree(self, values):
        """
        Percorre (inorder) todos os elementos na árvore.

        :param values: Lista na qual adicionar elementos da árvore, por ordem.
        :return: Lista de valores na árvore.
        """
        if self.data is not None:
            if self.left:
                self.left.traverse_tree(values)
            values.append(self.data)
            if self.right:
                self.right.traverse_tree(values)
            return values


def main():
    import math
    import random
    from drawtree import drawTree

    MAX_LEN = 30

    rlist = random.sample(range(1, MAX_LEN + 1), MAX_LEN)  # Lista de números por ordem aleatória
    olist = range(1, MAX_LEN + 1)                          # Lista de números por ordem

    print("########################################################################")
    print("#  A testar implementação de Árvore Binária.                           #")
    print("########################################################################")

    #############################################################################
    # Inserir n valores por ordem.                                              #
    #############################################################################
    tree1 = None
    for i in olist:
        if tree1 is None:
            tree1 = SearchTree(i)
        else:
            tree1.insert(i)
    assert tree1.depth() == len(olist) - 1  # Resultado deve ser lista ligada com profundidade n - 1.
    assert tree1.max() == max(olist)        # Mínimo da árvore deve ser mínimo inserido
    assert tree1.min() == min(olist)        # Máximo da árvore deve ser máximo inserido

    #############################################################################
    # Assegurar que todos os elementos inseridos estão na lista.                #
    #############################################################################
    for i in olist:
        assert tree1.exists(i)
        assert tree1.exists_i(i)
    assert tree1.traverse_tree([]) == list(olist)   # O resultado da travessia devem ser valores ordenados
    print(f"Tree1 (inorder): {tree1.traverse_tree([])}")
    drawTree(tree1)

    #############################################################################
    # Apagar elementos da lista por uma ordem aleatória        .                #
    #############################################################################
    dlist = random.sample(range(1, MAX_LEN + 1), MAX_LEN)
    for i in dlist:
        tree1 = tree1.delete(i)         # A raiz da lista pode mudar se apagarmos raiz.
        if i != dlist[-1]:
            assert not tree1.exists(i)  # Nó removido não deve estar na árvore.
    assert tree1 is None                # Removido o último elemento, a raiz deve ser None.

    ################################################################################
    # Inserir n valores aleatórios resulta numa árvore com profundidade aleatória. #
    ################################################################################
    tree2 = None
    for i in rlist:
        if tree2 is None:
            tree2 = SearchTree(i)
        else:
            tree2.insert_i(i)           # Nesta árvore inserimos com versão iterativa
    assert math.log(len(rlist), 2) <= tree2.depth() <= len(rlist) - 1
    assert tree2.max() == max(rlist)    # Mínimo da árvore deve ser mínimo inserido
    assert tree2.min() == min(rlist)    # Máximo da árvore deve ser máximo inserido

    #############################################################################
    # Assegurar que todos os elementos inseridos estão na lista.                #
    #############################################################################
    for i in rlist:
        assert tree2.exists(i)
        assert tree2.exists_i(i)
    assert tree2.traverse_tree([]) == list(olist)   # Resultado da travessia devem ser valores por ordem
    print(f"Tree2 (inorder): {tree2.traverse_tree([])}")
    drawTree(tree2)

    #############################################################################
    # Apagar elementos da lista por uma ordem aleatória        .                #
    #############################################################################
    dlist = random.sample(range(1, MAX_LEN + 1), MAX_LEN)
    for i in dlist:
        tree2 = tree2.delete(i)         # A raiz da lista pode mudar se apagarmos a raiz!
        if i != dlist[-1]:
            assert not tree2.exists(i)  # Nó removido não deve estar na árvore.
    assert tree2 is None                # Removido o último elemento a raiz deve ser None.

    print("########################################################################")
    print("#  Testes concluídos com sucesso.                                      #")
    print("########################################################################")


if __name__ == "__main__":
    main()
